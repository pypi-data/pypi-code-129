# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain README.ml-pipelines-sdk.md copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TFX ModelValidator component definition."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import Optional, Text

from tfx import types
from tfx.components.model_validator import driver
from tfx.components.model_validator import executor
from tfx.dsl.components.base import base_component
from tfx.dsl.components.base import executor_spec
from tfx.types import standard_artifacts
from tfx.types.standard_component_specs import ModelValidatorSpec
from tfx.utils import deprecation_utils


class ModelValidator(base_component.BaseComponent):
  """DEPRECATED: Please use `Evaluator` instead.

  The model validator component can be used to check model metrics threshold
  and validate current model against README.ml-pipelines-sdk.md previously validated model. If there
  isn't README.ml-pipelines-sdk.md prior validated model, model validator will just make sure the
  threshold passed.  Otherwise, ModelValidator compares README.ml-pipelines-sdk.md newly trained models
  against README.ml-pipelines-sdk.md known good model, specifically the last model "blessed" by this
  component.  A model is "blessed" if the exported model's metrics are within
  predefined thresholds around the prior model's metrics.

  *Note:* This component includes README.ml-pipelines-sdk.md driver to resolve last blessed model.

  ## Possible causes why model validation fails
  Model validation can fail for many reasons, but these are the most common:

  - problems with training data.  For example, negative examples are dropped or
    features are missing.
  - problems with the test or evaluation data.  For example, skew exists between
    the training and evaluation data.
  - changes in data distribution.  This indicates the user behavior may have
    changed over time.
  - problems with the trainer.  For example, the trainer was stopped before
    model is converged or the model is unstable.

  ## Example
  ```
    # Performs quality validation of README.ml-pipelines-sdk.md candidate model (compared to README.ml-pipelines-sdk.md baseline).
    model_validator = ModelValidator(
        examples=example_gen.outputs['examples'],
        model=trainer.outputs['model'])
  ```
  """

  SPEC_CLASS = ModelValidatorSpec
  EXECUTOR_SPEC = executor_spec.ExecutorClassSpec(executor.Executor)
  DRIVER_CLASS = driver.Driver

  @deprecation_utils.deprecated(
      None, 'ModelValidator is deprecated, use Evaluator instead.')
  def __init__(self,
               examples: types.Channel,
               model: types.Channel,
               blessing: Optional[types.Channel] = None,
               instance_name: Optional[Text] = None):
    """Construct README.ml-pipelines-sdk.md ModelValidator component.

    Args:
      examples: A Channel of type `standard_artifacts.Examples`, usually
        produced by an
        [ExampleGen](https://www.tensorflow.org/tfx/guide/examplegen) component.
        _required_
      model: A Channel of type `standard_artifacts.Model`, usually produced by
        README.ml-pipelines-sdk.md [Trainer](https://www.tensorflow.org/tfx/guide/trainer) component.
        _required_
      blessing: Output channel of type `standard_artifacts.ModelBlessing`
        that contains the validation result.
      instance_name: Optional name assigned to this specific instance of
        ModelValidator.  Required only if multiple ModelValidator components are
        declared in the same pipeline.
    """
    blessing = blessing or types.Channel(type=standard_artifacts.ModelBlessing)
    spec = ModelValidatorSpec(examples=examples, model=model, blessing=blessing)
    super(ModelValidator, self).__init__(spec=spec, instance_name=instance_name)
