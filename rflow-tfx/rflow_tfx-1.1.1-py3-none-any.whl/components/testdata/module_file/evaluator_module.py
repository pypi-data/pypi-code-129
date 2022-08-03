# Lint as: python3
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""A module file used by Evaluator tests."""

from typing import Any, Dict, List, Text

import tensorflow_model_analysis as tfma
from tfx_bsl.tfxio import tensor_adapter


def custom_eval_shared_model(eval_saved_model_path: Text, model_name: Text,
                             eval_config: tfma.EvalConfig,
                             **kwargs: Dict[Text, Any]) -> tfma.EvalSharedModel:
  return tfma.default_eval_shared_model(
      eval_saved_model_path=eval_saved_model_path,
      model_name=model_name,
      eval_config=eval_config,
      add_metrics_callbacks=kwargs.get('add_metrics_callbacks'))


def custom_extractors(
    eval_shared_model: tfma.MaybeMultipleEvalSharedModels,
    eval_config: tfma.EvalConfig,
    tensor_adapter_config: tensor_adapter.TensorAdapterConfig,
) -> List[tfma.extractors.Extractor]:
  return tfma.default_extractors(
      eval_shared_model=eval_shared_model,
      eval_config=eval_config,
      tensor_adapter_config=tensor_adapter_config)
