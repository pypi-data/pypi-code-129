# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfx/proto/evaluator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfx/proto/evaluator.proto',
  package='tfx.components.evaluator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19tfx/proto/evaluator.proto\x12\x18tfx.components.evaluator\"5\n\x11SingleSlicingSpec\x12\x1a\n\x12\x63olumn_for_slicing\x18\x01 \x03(\tJ\x04\x08\x02\x10\x03\"V\n\x12\x46\x65\x61tureSlicingSpec\x12:\n\x05specs\x18\x01 \x03(\x0b\x32+.tfx.components.evaluator.SingleSlicingSpecJ\x04\x08\x02\x10\x03\x62\x06proto3')
)




_SINGLESLICINGSPEC = _descriptor.Descriptor(
  name='SingleSlicingSpec',
  full_name='tfx.components.evaluator.SingleSlicingSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='column_for_slicing', full_name='tfx.components.evaluator.SingleSlicingSpec.column_for_slicing', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=108,
)


_FEATURESLICINGSPEC = _descriptor.Descriptor(
  name='FeatureSlicingSpec',
  full_name='tfx.components.evaluator.FeatureSlicingSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='specs', full_name='tfx.components.evaluator.FeatureSlicingSpec.specs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=196,
)

_FEATURESLICINGSPEC.fields_by_name['specs'].message_type = _SINGLESLICINGSPEC
DESCRIPTOR.message_types_by_name['SingleSlicingSpec'] = _SINGLESLICINGSPEC
DESCRIPTOR.message_types_by_name['FeatureSlicingSpec'] = _FEATURESLICINGSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingleSlicingSpec = _reflection.GeneratedProtocolMessageType('SingleSlicingSpec', (_message.Message,), {
  'DESCRIPTOR' : _SINGLESLICINGSPEC,
  '__module__' : 'tfx.proto.evaluator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.evaluator.SingleSlicingSpec)
  })
_sym_db.RegisterMessage(SingleSlicingSpec)

FeatureSlicingSpec = _reflection.GeneratedProtocolMessageType('FeatureSlicingSpec', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESLICINGSPEC,
  '__module__' : 'tfx.proto.evaluator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.evaluator.FeatureSlicingSpec)
  })
_sym_db.RegisterMessage(FeatureSlicingSpec)


# @@protoc_insertion_point(module_scope)
