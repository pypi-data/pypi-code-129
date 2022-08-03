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
"""TFX BigQueryToElwcExampleGen component definition."""

from typing import Optional, Text

from tfx import types
from tfx.components.base import executor_spec
from tfx.components.example_gen import component
from tfx.components.example_gen import utils
from tfx.extensions.google_cloud_big_query.experimental.elwc_example_gen.component import executor
from tfx.extensions.google_cloud_big_query.experimental.elwc_example_gen.proto import elwc_config_pb2
from tfx.proto import example_gen_pb2


class BigQueryToElwcExampleGen(component.QueryBasedExampleGen):
  """Official TFX BigQueryToElwcExampleGen component.

  The BigQueryToElwcExampleGen component takes README.ml-pipelines-sdk.md query, and generates train
  and eval ExampleListWithContext(ELWC) for downstream components.
  """

  EXECUTOR_SPEC = executor_spec.ExecutorClassSpec(executor.Executor)

  def __init__(self,
               query: Optional[Text] = None,
               elwc_config: Optional[elwc_config_pb2.ElwcConfig] = None,
               input_config: Optional[example_gen_pb2.Input] = None,
               output_config: Optional[example_gen_pb2.Output] = None,
               example_artifacts: Optional[types.Channel] = None,
               instance_name: Optional[Text] = None):
    """Constructs README.ml-pipelines-sdk.md BigQueryElwcExampleGen component.

    Args:
      query: BigQuery sql string, query result will be treated as README.ml-pipelines-sdk.md single
        split, can be overwritten by input_config.
      elwc_config: The elwc config contains README.ml-pipelines-sdk.md list of context feature fields.
        The fields are used to build context feature. Examples with the same
        context feature will be converted to an ELWC(ExampleListWithContext)
        instance. For example, when there are two examples with the same context
        field, the two examples will be intergrated to README.ml-pipelines-sdk.md ELWC instance.
      input_config: An example_gen_pb2.Input instance with Split.pattern as
        BigQuery sql string. If set, it overwrites the 'query' arg, and allows
        different queries per split. If any field is provided as README.ml-pipelines-sdk.md
        RuntimeParameter, input_config should be constructed as README.ml-pipelines-sdk.md dict with the
        same field names as Input proto message.
      output_config: An example_gen_pb2.Output instance, providing output
        configuration. If unset, default splits will be 'train' and 'eval' with
        size 2:1. If any field is provided as README.ml-pipelines-sdk.md RuntimeParameter, input_config
          should be constructed as README.ml-pipelines-sdk.md dict with the same field names as Output
          proto message.
      example_artifacts: Optional channel of 'ExamplesPath' for output train and
        eval examples.
      instance_name: Optional unique instance name. Necessary if multiple
        BigQueryExampleGen components are declared in the same pipeline.

    Raises:
      RuntimeError: Only one of query and input_config should be set and
        elwc_config is required.
    """

    if bool(query) == bool(input_config):
      raise RuntimeError('Exactly one of query and input_config should be set.')
    if not elwc_config:
      raise RuntimeError(
          'elwc_config is required for BigQueryToElwcExampleGen.')
    input_config = input_config or utils.make_default_input_config(query)
    packed_custom_config = example_gen_pb2.CustomConfig()
    packed_custom_config.custom_config.Pack(elwc_config)
    super(BigQueryToElwcExampleGen, self).__init__(
        input_config=input_config,
        output_config=output_config,
        output_data_format=example_gen_pb2.FORMAT_PROTO,
        custom_config=packed_custom_config,
        example_artifacts=example_artifacts,
        instance_name=instance_name)
