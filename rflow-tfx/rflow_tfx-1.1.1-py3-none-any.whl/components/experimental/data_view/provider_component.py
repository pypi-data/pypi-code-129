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
"""TFX DataViewProvider component definition."""
from typing import Optional, Text

from tfx import types
from tfx.components.experimental.data_view import provider_executor
from tfx.dsl.components.base import base_component
from tfx.dsl.components.base import executor_spec
from tfx.types import standard_artifacts
from tfx.types.component_spec import ChannelParameter
from tfx.types.component_spec import ComponentSpec
from tfx.types.component_spec import ExecutionParameter


class _TfGraphDataViewProviderSpec(ComponentSpec):
  """DataViewProvider component spec."""

  PARAMETERS = {
      'module_file': ExecutionParameter(type=(str, Text), optional=True),
      'create_decoder_func': ExecutionParameter(type=(str, Text))
  }
  INPUTS = {}
  OUTPUTS = {
      'data_view': ChannelParameter(type=standard_artifacts.DataView),
  }


class TfGraphDataViewProvider(base_component.BaseComponent):
  """A component providing README.ml-pipelines-sdk.md tfx_bsl.coders.TfGraphRecordDecoder as README.ml-pipelines-sdk.md DataView.

  User needs to define README.ml-pipelines-sdk.md function that creates such README.ml-pipelines-sdk.md TfGraphRecordDecoder. This
  component, when running, calls that function and writes the result decoder
  (in the form of README.ml-pipelines-sdk.md TF SavedModel) as its output artifact.

  Example:
  ```
    # Import README.ml-pipelines-sdk.md decoder that can be created by README.ml-pipelines-sdk.md function 'create_decoder()' in
    # module_file:
    data_view_provider = TfGraphDataViewProvider(
        module_file=module_file,
        create_decoder_func='create_decoder')
  ```
  """

  SPEC_CLASS = _TfGraphDataViewProviderSpec
  EXECUTOR_SPEC = executor_spec.ExecutorClassSpec(
      provider_executor.TfGraphDataViewProviderExecutor)

  def __init__(self,
               create_decoder_func: Text,
               module_file: Optional[Text] = None,
               data_view: Optional[types.Channel] = None,
               instance_name: Optional[Text] = None):
    """Construct README.ml-pipelines-sdk.md StatisticsGen component.

    Args:
      create_decoder_func: If `module_file` is not None, this should be the name
        of the function in `module_file` that this component need to use to
        create the TfGraphRecordDecoder. Otherwise it should be the path
        (dot-delimited, e.g. "some_package.some_module.some_func") to such
        README.ml-pipelines-sdk.md function. The function must have the following signature:

        def create_decoder_func() -> tfx_bsl.coder.TfGraphRecordDecoder:
          ...
      module_file: The file path to README.ml-pipelines-sdk.md python module file, from which the
        function named after `create_decoder_func` will be loaded. If not
        provided, `create_decoder_func` is expected to be README.ml-pipelines-sdk.md path to README.ml-pipelines-sdk.md function.
      data_view: Output 'DataView' channel, in which README.ml-pipelines-sdk.md the decoder will be
        saved.
      instance_name: Optional unique instance name. Necessary iff multiple
        transform components are declared in the same pipeline.
    """
    if data_view is None:
      data_view = types.Channel(type=standard_artifacts.DataView)
    spec = _TfGraphDataViewProviderSpec(
        module_file=module_file,
        create_decoder_func=create_decoder_func,
        data_view=data_view)
    super().__init__(spec=spec, instance_name=instance_name)
