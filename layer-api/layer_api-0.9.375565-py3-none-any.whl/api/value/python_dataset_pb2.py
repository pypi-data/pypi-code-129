# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/python_dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.value import python_source_pb2 as api_dot_value_dot_python__source__pb2
from layerapi.api.value import s3_path_pb2 as api_dot_value_dot_s3__path__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/value/python_dataset.proto\x12\x03\x61pi\x1a\x1d\x61pi/value/python_source.proto\x1a\x17\x61pi/value/s3_path.proto\"g\n\rPythonDataset\x12\x1c\n\x07s3_path\x18\x01 \x01(\x0b\x32\x0b.api.S3Path\x12(\n\rpython_source\x18\x02 \x01(\x0b\x32\x11.api.PythonSource\x12\x0e\n\x06\x66\x61\x62ric\x18\x03 \x01(\tB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_PYTHONDATASET = DESCRIPTOR.message_types_by_name['PythonDataset']
PythonDataset = _reflection.GeneratedProtocolMessageType('PythonDataset', (_message.Message,), {
  'DESCRIPTOR' : _PYTHONDATASET,
  '__module__' : 'api.value.python_dataset_pb2'
  # @@protoc_insertion_point(class_scope:api.PythonDataset)
  })
_sym_db.RegisterMessage(PythonDataset)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _PYTHONDATASET._serialized_start=95
  _PYTHONDATASET._serialized_end=198
# @@protoc_insertion_point(module_scope)
