# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Fit 2 GMMs to 2 point clouds using likelihood and (approx) W2 distance.

Suppose we have two large point clouds and want to estimate a coupling and a
W2 distance between them. :cite:`delon:20` propose fitting a GMM to each
point cloud while simultaneously minimizing a Wasserstein-like distance
called MW2 between the fitted GMMs. MW2 is an upper bound on W2,
the Wasserstein distance between the GMMs. Here we implement
their algorithm as well as a generalization that allows for reweightings using
generalized, penalized expectation-maximization
(see section 6.2 of :cite:`delon:20`).

As in `fit_gmm.py`, we assume that the observations $X_0$ and $X_1$ from
batches 0 and 1 are generated by GMMs with parameters $\Theta_0$ and $\Theta_1$,
respectively. We will use $\Theta$ to denote the combined parameters
for the two GMMs. We denote the (unobserved) components that gave rise to the
observations $X_i$ as $Z_i$.

Our goal is to maximize a weighted sum of the likelihood of the observations $X$
under the fitted GMMs and a measure of distance, $MW_2$, between the fitted
GMMs. The problem would be a straightforward maximization exercise if we knew
the components $Z$ that generated each observation $X$. Because the $Z$ are
unobserved, however, we use EM:

We start with an initial estimate of $\Theta$, $\Theta^{(t)}$.

* The E-step: We use the current $\Theta^{(t)}$ to estimate the likelihood of
  all possible cluster attributions for each observation $X$.

* The M-step: We form the function $Q(\Theta|\Theta^{(t)})$,
  the log likelihood of our observations averaged over all possible
  assignments. We then obtain an updated parameter estimate, $\Theta^{(t+1)}$,
  by numerically maximizing the sum of $Q$ and our GMM distance penalty.

It can be shown that if we maximize the penalized $Q$ above, this procedure will
increase or leave unchanged the penalized log likelihood for $\Theta$. We
iterate over these two steps until convergence. Note that the resulting
estimate for $\Theta$ may only be a *local* maximum of the penalized
likelihood function.


Sample usage:

# (Note that we usually initialize a pair to a single GMM that we fit to a
# pooled set, then the two GMMs separate as we optimize the pair.)
pair_init = gaussian_mixture_pair.GaussianMixturePair(
    gmm0=gmm0,
    gmm1=gmm1,
    epsilon=1.e-2,
    tau=1.)
fit_model_em_fn = fit_gmm_pair.get_fit_model_em_fn(
    weight_transport=0.1,
    weight_splitting=1.,
    epsilon=pair_init.epsilon,
    jit=True)
pair, loss = fit_model_em_fn(
    pair=pair_init,
    points0=samples_gmm0,
    points1=samples_gmm1,
    point_weights0=None,
    point_weights1=None,
    em_steps=30,
    m_steps=20,
    verbose=True)
"""
# TODO(geoffd): look into refactoring so we jit higher level functions

import functools
import math
from typing import Callable, NamedTuple, Optional, Tuple

import jax
import jax.numpy as jnp
import optax

from ott.tools.gaussian_mixture import fit_gmm, gaussian_mixture, gaussian_mixture_pair

LOG2 = math.log(2)


class Observations(NamedTuple):
  """Weighted observations and their E-step assignment probabilities."""

  points: jnp.ndarray
  point_weights: jnp.ndarray
  assignment_probs: jnp.ndarray


# Model fit


def get_q(
    gmm: gaussian_mixture.GaussianMixture, obs: Observations
) -> jnp.ndarray:
  r"""Get Q(\Theta|\Theta^{(t)}).

  Here Q is the log likelihood for our observations based on the current
  parameter estimates for \Theta and averaged over the current component
  assignment probabilities. See the overview of EM above for more details.

  Args:
    gmm: GMM model parameterized by Theta
    obs: weighted observations with component assignments computed in the E step
      for \Theta^{(t)}

  Returns:
    Q(\Theta|\Theta^{(t)})
  """
  # Q = E_Z log p(X, Z| Theta)
  # = \sum_Z P(Z|X, Theta^(t)) [log p(X, Z | Theta)]
  # Here P(Z|X, theta^(t)) is the set of assignment probabilities
  # we computed in the E step.
  # log p(X, Z| theta) is given by
  log_p_x_z = (
      gmm.conditional_log_prob(obs.points) +  # p(X | Z, theta)
      gmm.log_component_weights()
  )  # p(Z | theta)
  return (
      jnp.sum(
          obs.point_weights *
          jnp.sum(log_p_x_z * obs.assignment_probs, axis=-1),
          axis=0
      ) / jnp.sum(obs.point_weights, axis=0)
  )


# Objective function


@functools.lru_cache
def get_objective_fn(weight_transport: float):
  """Get the total loss function with static parameters in a closure.

  Args:
    weight_transport: weight for the transport penalty

  Returns:
    A function that returns the objective for a GaussianMixturePair.
  """

  def _objective_fn(
      pair: gaussian_mixture_pair.GaussianMixturePair,
      obs0: Observations,
      obs1: Observations,
  ) -> jnp.ndarray:
    """Compute the objective function for a pair of GMMs.

    Args:
      pair: pair of GMMs + coupling for which to evaluate the objective
      obs0: first set of observations
      obs1: second set of observations

    Returns:
      The objective to be minimized in the M-step.
    """
    q0 = get_q(gmm=pair.gmm0, obs=obs0)
    q1 = get_q(gmm=pair.gmm1, obs=obs1)
    cost_matrix = pair.get_cost_matrix()
    sinkhorn_output = pair.get_sinkhorn(cost_matrix=cost_matrix)
    transport_penalty = sinkhorn_output.reg_ot_cost
    return q0 + q1 - weight_transport * transport_penalty

  return _objective_fn


def print_losses(
    iteration: int, weight_transport: float,
    pair: gaussian_mixture_pair.GaussianMixturePair, obs0: Observations,
    obs1: Observations
):
  """Print the loss components for diagnostic purposes."""
  q0 = get_q(gmm=pair.gmm0, obs=obs0)
  q1 = get_q(gmm=pair.gmm1, obs=obs1)
  cost_matrix = pair.get_cost_matrix()
  sinkhorn_output = pair.get_sinkhorn(cost_matrix=cost_matrix)
  transport_penalty = sinkhorn_output.reg_ot_cost
  objective = q0 + q1 - weight_transport * transport_penalty

  print((
      f'{iteration:3d} {q0:.3f} {q1:.3f} '
      f'transport:{transport_penalty:.3f} '
      f'objective:{objective:.3f}'
  ),
        flush=True)


# The E-step for a single GMM


def do_e_step(
    e_step_fn: Callable[[gaussian_mixture.GaussianMixture, jnp.ndarray],
                        jnp.ndarray],
    gmm: gaussian_mixture.GaussianMixture,
    points: jnp.ndarray,
    point_weights: jnp.ndarray,
) -> Observations:
  assignment_probs = e_step_fn(gmm, points)
  return Observations(
      points=points,
      point_weights=point_weights,
      assignment_probs=assignment_probs
  )


# The M-step


def get_m_step_fn(learning_rate: float, objective_fn, jit: bool):
  """Get a function that performs the M-step of the EM algorithm.

  We precompile and precompute a few quantities that we put into a closure.

  Args:
    learning_rate: learning rate to use for the Adam optimizer
    objective_fn: the objective function to maximize
    jit: if True, precompile key methods

  Returns:
    A function that performs the M-step of EM.
  """
  grad_objective_fn = jax.grad(objective_fn, argnums=(0,))
  gmm_m_step_fn = gaussian_mixture.GaussianMixture.from_points_and_assignment_probs
  if jit:
    grad_objective_fn = jax.jit(grad_objective_fn)
    gmm_m_step_fn = jax.jit(gmm_m_step_fn)

  opt_init, opt_update = optax.chain(
      # Set the parameters of Adam. Note the learning_rate is not here.
      optax.scale_by_adam(b1=0.9, b2=0.999, eps=1e-8),
      optax.scale(learning_rate)
  )

  def _m_step_fn(
      pair: gaussian_mixture_pair.GaussianMixturePair,
      obs0: Observations,
      obs1: Observations,
      steps: int,
  ) -> gaussian_mixture_pair.GaussianMixturePair:
    """Perform the M-step on a pair of Gaussian mixtures.

    Args:
      pair: GMM parameters to optimize
      obs0: first set of observations
      obs1: second set of observations
      steps: number of optimization steps to use when maximizing the objective

    Returns:
      A GaussianMixturePair with updated parameters.
    """
    params = (pair,)
    state = opt_init(params)

    for _ in range(steps):
      grad_objective = grad_objective_fn(pair, obs0, obs1)
      updates, state = opt_update(grad_objective, state, params)
      params = optax.apply_updates(params, updates)
      for j, gmm in enumerate((params[0].gmm0, params[0].gmm1)):
        if gmm.has_nans():
          raise ValueError(f'NaN in gmm{j}')
    return params[0]

  return _m_step_fn


def get_fit_model_em_fn(
    weight_transport: float,
    learning_rate: float = 0.001,
    jit: bool = True,
):
  """Get a function that performs penalized EM.

  We precompile and precompute a few quantities that we put into a closure.

  Args:
    weight_transport: weight for the transportation loss in the total loss
    learning_rate: learning rate to use for the Adam optimizer
    jit: if True, precompile key methods

  Returns:
    A function that performs generalized, penalized EM.
  """
  objective_fn = get_objective_fn(weight_transport=weight_transport)
  e_step_fn = fit_gmm.get_assignment_probs

  if jit:
    objective_fn = jax.jit(objective_fn)
    e_step_fn = jax.jit(e_step_fn)

  m_step_fn = get_m_step_fn(
      learning_rate=learning_rate, objective_fn=objective_fn, jit=jit
  )

  def _fit_model_em(
      pair: gaussian_mixture_pair.GaussianMixturePair,
      points0: jnp.ndarray,
      points1: jnp.ndarray,
      point_weights0: Optional[jnp.ndarray],
      point_weights1: Optional[jnp.ndarray],
      em_steps: int,
      m_steps: int = 50,
      verbose: bool = False,
  ) -> Tuple[gaussian_mixture_pair.GaussianMixturePair, float]:
    """Optimize a GaussianMixturePair using penalized EM.

    Args:
      pair: GaussianMixturePair to optimize
      points0: observations associated with pair.gmm0
      points1: observations associated with pair.gmm1
      point_weights0: weights for points0
      point_weights1: weights for points1
      em_steps: number of EM steps to perform
      m_steps: number of gradient descent steps to perform in the M-step
      verbose: if True, print status messages

    Returns:
      An updated GaussianMixturePair and the final loss.
    """
    if point_weights0 is None:
      point_weights0 = jnp.ones(points0.shape[0])
    if point_weights1 is None:
      point_weights1 = jnp.ones(points1.shape[0])

    if pair.lock_gmm1:
      obs1 = do_e_step(
          e_step_fn=e_step_fn,
          gmm=pair.gmm1,
          points=points1,
          point_weights=point_weights1
      )

    for i in range(em_steps):
      # E-step
      obs0 = do_e_step(
          e_step_fn=e_step_fn,
          gmm=pair.gmm0,
          points=points0,
          point_weights=point_weights0
      )
      if not pair.lock_gmm1:
        obs1 = do_e_step(
            e_step_fn=e_step_fn,
            gmm=pair.gmm1,
            points=points1,
            point_weights=point_weights1
        )

      # print current losses
      if verbose:
        print_losses(
            iteration=i,
            weight_transport=weight_transport,
            pair=pair,
            obs0=obs0,
            obs1=obs1
        )

      # the M-step
      pair = m_step_fn(pair=pair, obs0=obs0, obs1=obs1, steps=m_steps)

    # final E-step before computing the loss
    obs0 = do_e_step(
        e_step_fn=e_step_fn,
        gmm=pair.gmm0,
        points=points0,
        point_weights=point_weights0
    )
    if not pair.lock_gmm1:
      obs1 = do_e_step(
          e_step_fn=e_step_fn,
          gmm=pair.gmm1,
          points=points1,
          point_weights=point_weights1
      )

    loss = objective_fn(pair=pair, obs0=obs0, obs1=obs1)
    return pair, loss

  return _fit_model_em
