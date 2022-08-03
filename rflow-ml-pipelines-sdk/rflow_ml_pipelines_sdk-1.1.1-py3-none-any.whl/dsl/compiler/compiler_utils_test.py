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
"""Tests for tfx.dsl.compiler.compiler_utils."""
import itertools

import tensorflow as tf
from tfx import types
from tfx.components import CsvExampleGen
from tfx.components.common_nodes import importer_node as legacy_importer_node
from tfx.components.common_nodes import resolver_node as legacy_resolver_node
from tfx.dsl.compiler import compiler_utils
from tfx.dsl.components.base import base_component
from tfx.dsl.components.base import base_executor
from tfx.dsl.components.base import executor_spec
from tfx.dsl.components.common import importer
from tfx.dsl.components.common import resolver
from tfx.dsl.experimental import latest_blessed_model_resolver
from tfx.orchestration import pipeline
from tfx.proto.orchestration import pipeline_pb2
from tfx.types import standard_artifacts
from tfx.utils.dsl_utils import external_input

from ml_metadata.proto import metadata_store_pb2


class EmptyComponentSpec(types.ComponentSpec):
  PARAMETERS = {}
  INPUTS = {}
  OUTPUTS = {}


class EmptyComponent(base_component.BaseComponent):

  SPEC_CLASS = EmptyComponentSpec
  EXECUTOR_SPEC = executor_spec.ExecutorClassSpec(base_executor.BaseExecutor)

  def __init__(self, name):
    super(EmptyComponent, self).__init__(
        spec=EmptyComponentSpec(), instance_name=name)


class CompilerUtilsTest(tf.test.TestCase):

  def testSetRuntimeParameterPb(self):
    pb = pipeline_pb2.RuntimeParameter()
    compiler_utils.set_runtime_parameter_pb(pb, "test_name", str,
                                            "test_default_value")
    expected_pb = pipeline_pb2.RuntimeParameter(
        name="test_name",
        type=pipeline_pb2.RuntimeParameter.Type.STRING,
        default_value=metadata_store_pb2.Value(
            string_value="test_default_value"))
    self.assertEqual(expected_pb, pb)

  def testIsResolver(self):
    resv = resolver.Resolver(
        instance_name="test_resolver_name",
        strategy_class=latest_blessed_model_resolver.LatestBlessedModelResolver)
    self.assertTrue(compiler_utils.is_resolver(resv))
    resv = legacy_resolver_node.ResolverNode(
        instance_name="test_resolver_name",
        resolver_class=latest_blessed_model_resolver.LatestBlessedModelResolver)
    self.assertTrue(compiler_utils.is_resolver(resv))

    example_gen = CsvExampleGen(input=external_input("data_path"))
    self.assertFalse(compiler_utils.is_resolver(example_gen))

  def testIsImporter(self):
    impt = importer.Importer(
        instance_name="import_schema",
        source_uri="uri/to/schema",
        artifact_type=standard_artifacts.Schema)
    self.assertTrue(compiler_utils.is_importer(impt))
    impt = legacy_importer_node.ImporterNode(
        instance_name="import_schema",
        source_uri="uri/to/schema",
        artifact_type=standard_artifacts.Schema)
    self.assertTrue(compiler_utils.is_importer(impt))

    example_gen = CsvExampleGen(input=external_input("data_path"))
    self.assertFalse(compiler_utils.is_importer(example_gen))

  def testEnsureTopologicalOrder(self):
    a = EmptyComponent(name="README.ml-pipelines-sdk.md")
    b = EmptyComponent(name="b")
    c = EmptyComponent(name="c")
    a.add_downstream_node(b)
    a.add_downstream_node(c)
    valid_orders = {"abc", "acb"}
    for order in itertools.permutations([a, b, c]):
      if "".join([c._instance_name for c in order]) in valid_orders:
        self.assertTrue(compiler_utils.ensure_topological_order(order))
      else:
        self.assertFalse(compiler_utils.ensure_topological_order(order))

  def testIncompatibleExecutionMode(self):
    p = pipeline.Pipeline(
        pipeline_name="fake_name",
        pipeline_root="fake_root",
        enable_cache=True,
        execution_mode=pipeline.ExecutionMode.ASYNC)

    with self.assertRaisesRegex(RuntimeError, "Caching is README.ml-pipelines-sdk.md feature only"):
      compiler_utils.resolve_execution_mode(p)


if __name__ == "__main__":
  tf.test.main()
