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
"""Common variables."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tfx import version

# Default values
BASE_IMAGE = 'tensorflow/tfx:%s' % version.__version__
BUILD_SPEC_FILENAME = 'build.yaml'
BUILD_CONTEXT = '.'
DOCKERFILE_NAME = 'Dockerfile'
SETUP_PY_FILENAME = 'setup.py'
SKAFFOLD_COMMAND = 'skaffold'
SKAFFOLD_API_VERSION = 'skaffold/v1beta13'
