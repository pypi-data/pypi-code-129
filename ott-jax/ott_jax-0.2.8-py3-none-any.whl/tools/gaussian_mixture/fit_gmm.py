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
r"""Fit a Gaussian mixture model.

Sample usage:

# initialize GMM with K-means++
gmm_init = fit_gmm.initialize(
  key=key,
  points=my_points,
  point_weights=None,
  n_components=COMPONENTS)

# refine GMM parameters using EM
gmm = fit_gmm.fit_model_em(
  gmm=gmm_init,
  points=my_points,
  point_weights=None,
  steps=10,
  verbose=True)


We fit the model using EM. Below we'll use notation following
https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm

Our data X is generated by a Gaussian mixture with unknown parameters \Theta.
We denote the (unobserved) component that gave rise to each point as Z.

In EM we start with an initial estimate of $\Theta$, $\Theta^{(0)}$, and we
then iteratively update it via

$$\Theta^{(t+1)} = \argmax_{\Theta} Q(\Theta|\Theta^{(t)})$$

where

$$
Q(\Theta|\Theta(t)) = E_{Z|X,\Theta^{(t)}} \left[ \log L(\Theta; X, Z) \right]
$$
"""

from typing import Optional

import jax
import jax.numpy as jnp

from ott.tools.gaussian_mixture import gaussian_mixture

# EM algorithm for parameter estimation


def get_assignment_probs(
    gmm: gaussian_mixture.GaussianMixture, points: jnp.ndarray
) -> jnp.ndarray:
  r"""Get component assignment probabilities used in the E step of EM.

  Here we compute the component assignment probabilities p(Z|X, \Theta^{(t)})
  that we need to compute the expectation used for Q(\Theta|\Theta^{(t)}).

  Args:
    gmm: GMM model
    points: set of samples being fitted, shape (n, n_dimensions)

  Returns:
    An array of assignment probabilities with shape (n, n_components)
  """
  return jnp.exp(gmm.get_log_component_posterior(points))


def get_q(
    gmm: gaussian_mixture.GaussianMixture,
    assignment_probs: jnp.ndarray,
    points: jnp.ndarray,
    point_weights: Optional[jnp.ndarray] = None,
) -> float:
  r"""Get Q(\Theta|\Theta^{(t)}).

  Args:
    gmm: GaussianMixture with parameters \Theta
    assignment_probs: p(Z|X, \Theta^{(t)}) as computed by get_assignment_probs
    points: observations X
    point_weights: optional set of weights for the samples. If None, use
      a weight of 1/n where n is the number of points.

  Returns:
    Q(\Theta|\Theta^{(t)})
  """
  # log P(X, Z| \Theta) = log P(X|Z, \Theta) + log P(Z|\Theta)
  loglik = (gmm.conditional_log_prob(points) + gmm.log_component_weights())
  if point_weights is None:
    point_weights = jnp.ones(points.shape[0])
  return (
      jnp.sum(point_weights * jnp.sum(assignment_probs * loglik, axis=-1)) /
      jnp.sum(point_weights)
  )


def log_prob_loss(
    gmm: gaussian_mixture.GaussianMixture,
    points: jnp.ndarray,
    point_weights: Optional[jnp.ndarray] = None,
) -> float:
  """Loss function: weighted mean of (-log prob of observations).

  Args:
    gmm: GMM model
    points: set of samples being fitted
    point_weights: optional set of weights for the samples. If None, use
      a weight of 1/n where n is the number of points.

  Returns:
    The GMM loss for the points.
  """
  if point_weights is None:
    return -jnp.mean(gmm.log_prob(points))
  return -jnp.sum(point_weights * gmm.log_prob(points)) / jnp.sum(point_weights)


def fit_model_em(
    gmm: gaussian_mixture.GaussianMixture,
    points: jnp.ndarray,
    point_weights: Optional[jnp.ndarray],
    steps: int,
    jit: bool = True,
    verbose: bool = False,
) -> gaussian_mixture.GaussianMixture:
  """Fit a GMM using the EM algorithm.

  Args:
    gmm: initial GMM model
    points: set of samples to fit, shape (n, n_dimensions)
    point_weights: optional set of weights for points, shape (n,). If None,
      uses equal weights for all points.
    steps: number of steps of EM to perform
    jit: if True, compile functions
    verbose: if True, print the loss at each step

  Returns:
    A GMM with updated parameters.
  """
  if point_weights is None:
    point_weights = jnp.ones(points.shape[:-1], dtype=points.dtype)
  loss_fn = log_prob_loss
  get_q_fn = get_q
  e_step_fn = get_assignment_probs
  m_step_fn = gaussian_mixture.GaussianMixture.from_points_and_assignment_probs
  if jit:
    loss_fn = jax.jit(loss_fn)
    get_q_fn = jax.jit(get_q_fn)
    e_step_fn = jax.jit(e_step_fn)
    m_step_fn = jax.jit(m_step_fn)

  for i in range(steps):
    assignment_probs = e_step_fn(gmm, points)
    gmm_new = m_step_fn(points, point_weights, assignment_probs)
    if gmm_new.has_nans():
      raise ValueError('NaNs in fit.')
    if verbose:
      loss = loss_fn(gmm_new, points, point_weights)
      q = get_q_fn(
          gmm=gmm_new,
          assignment_probs=assignment_probs,
          points=points,
          point_weights=point_weights
      )
      print(f'{i}  q={q}  -log prob={loss}', flush=True)
    gmm = gmm_new
  return gmm


# KMeans++ for initialization
# See https://en.wikipedia.org/wiki/K-means%2B%2B for details


def _get_dist_sq(points: jnp.ndarray, loc: jnp.ndarray) -> jnp.ndarray:
  """Get the squared distance from each point to each loc."""

  def _dist_sq_one_loc(points: jnp.ndarray, loc: jnp.ndarray):
    return jnp.sum((points - loc[None]) ** 2., axis=-1)

  dist_sq_fn = jax.vmap(_dist_sq_one_loc, in_axes=(None, 0), out_axes=1)
  return dist_sq_fn(points, loc)


def _get_locs(
    key: jnp.ndarray, points: jnp.ndarray, n_components: int
) -> jnp.ndarray:
  """Get the initial component means.

  Args:
    key: jax.random seed
    points: (n, n_dimensions) array of observations
    n_components: desired number of components

  Returns:
    (n_components, n_dimensions) array of means.
  """
  points = points.copy()
  n_points = points.shape[0]
  weights = jnp.ones(n_points) / n_points
  key, subkey = jax.random.split(key)
  index = jax.random.choice(key=subkey, a=points.shape[0], p=weights)
  loc = points[index]
  points = jnp.concatenate([points[:index], points[index + 1:]], axis=0)

  locs = loc[None]
  for _ in range(n_components - 1):
    dist_sq = _get_dist_sq(points, locs)
    min_dist_sq = jnp.min(dist_sq, axis=-1)
    weights = min_dist_sq / jnp.sum(min_dist_sq)
    key, subkey = jax.random.split(key)
    index = jax.random.choice(key=subkey, a=points.shape[0], p=weights)
    loc = points[index]
    points = jnp.concatenate([points[:index], points[index + 1:]], axis=0)
    locs = jnp.concatenate([locs, loc[None]], axis=0)
  return locs


def from_kmeans_plusplus(
    key: jnp.ndarray,
    points: jnp.ndarray,
    point_weights: Optional[jnp.ndarray],
    n_components: int,
) -> gaussian_mixture.GaussianMixture:
  """Initialize a GMM via a single pass of K-means++.

  Args:
    key: jax.random seed
    points: (n, n_dimensions) array of observations
    point_weights: (n,) array of weights for points
    n_components: desired number of components

  Returns:
    An initial Gaussian mixture model.

  Raises:
    ValueError if any fitted parameters are non-finite.
  """
  key, subkey = jax.random.split(key)
  locs = _get_locs(key=subkey, points=points, n_components=n_components)
  dist_sq = _get_dist_sq(points, locs)
  assignment_prob = (dist_sq == jnp.min(dist_sq,
                                        axis=-1)[:, None]).astype(points.dtype)
  del dist_sq

  if point_weights is None:
    point_weights = jnp.ones_like(points[..., 0])
  return gaussian_mixture.GaussianMixture.from_points_and_assignment_probs(
      points=points,
      point_weights=point_weights,
      assignment_probs=assignment_prob
  )


def initialize(
    key: jnp.ndarray,
    points: jnp.ndarray,
    point_weights: Optional[jnp.ndarray],
    n_components: jnp.ndarray,
    n_attempts=50,
    verbose=False
) -> gaussian_mixture.GaussianMixture:
  """Initialize a GMM via K-means++ with retries on failure.

  Args:
    key: jax.random seed
    points: (n, n_dimensions) array of observations
    point_weights: (n,) array of weights for points
    n_components: desired number of components
    n_attempts: number of attempts to initialize before failing
    verbose: if True, print status information

  Returns:
    An initial Gaussian mixture model.

  Raises:
    ValueError if initialization was unsuccessful after n_attempts attempts.
  """
  for attempt in range(n_attempts):
    key, subkey = jax.random.split(key)
    try:
      gmm = from_kmeans_plusplus(
          key=subkey,
          points=points,
          point_weights=point_weights,
          n_components=n_components
      )
    except ValueError:
      if verbose:
        print(f'Failed to initialize, attempt {attempt}', flush=True)
    return gmm
  raise ValueError('Failed to initialize')
