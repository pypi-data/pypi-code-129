# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfx/proto/infra_validator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfx/proto/infra_validator.proto',
  package='tfx.components.infra_validator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ftfx/proto/infra_validator.proto\x12\x1etfx.components.infra_validator\"\xab\x02\n\x0bServingSpec\x12O\n\x12tensorflow_serving\x18\x01 \x01(\x0b\x32\x31.tfx.components.infra_validator.TensorFlowServingH\x00\x12I\n\x0clocal_docker\x18\x02 \x01(\x0b\x32\x31.tfx.components.infra_validator.LocalDockerConfigH\x01\x12\x46\n\nkubernetes\x18\x03 \x01(\x0b\x32\x30.tfx.components.infra_validator.KubernetesConfigH\x01\x12\x12\n\nmodel_name\x18\x04 \x01(\tB\x10\n\x0eserving_binaryB\x12\n\x10serving_platform\"F\n\x11TensorFlowServing\x12\x12\n\nimage_name\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x0f\n\x07\x64igests\x18\x02 \x03(\t\"h\n\x11LocalDockerConfig\x12\x17\n\x0f\x63lient_base_url\x18\x01 \x01(\t\x12\x1a\n\x12\x63lient_api_version\x18\x02 \x01(\t\x12\x1e\n\x16\x63lient_timeout_seconds\x18\x03 \x01(\x05\"Q\n\x10KubernetesConfig\x12\x1c\n\x14service_account_name\x18\x01 \x01(\t\x12\x1f\n\x17\x61\x63tive_deadline_seconds\x18\x02 \x01(\x05\"E\n\x0eValidationSpec\x12 \n\x18max_loading_time_seconds\x18\x01 \x01(\x05\x12\x11\n\tnum_tries\x18\x02 \x01(\x05\"\x9b\x01\n\x0bRequestSpec\x12Z\n\x12tensorflow_serving\x18\x01 \x01(\x0b\x32<.tfx.components.infra_validator.TensorFlowServingRequestSpecH\x00\x12\x12\n\nsplit_name\x18\x02 \x01(\t\x12\x14\n\x0cnum_examples\x18\x03 \x01(\x05\x42\x06\n\x04kind\"H\n\x1cTensorFlowServingRequestSpec\x12\x0f\n\x07tag_set\x18\x01 \x03(\t\x12\x17\n\x0fsignature_names\x18\x02 \x03(\tb\x06proto3')
)




_SERVINGSPEC = _descriptor.Descriptor(
  name='ServingSpec',
  full_name='tfx.components.infra_validator.ServingSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensorflow_serving', full_name='tfx.components.infra_validator.ServingSpec.tensorflow_serving', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_docker', full_name='tfx.components.infra_validator.ServingSpec.local_docker', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kubernetes', full_name='tfx.components.infra_validator.ServingSpec.kubernetes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='tfx.components.infra_validator.ServingSpec.model_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='serving_binary', full_name='tfx.components.infra_validator.ServingSpec.serving_binary',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='serving_platform', full_name='tfx.components.infra_validator.ServingSpec.serving_platform',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=68,
  serialized_end=367,
)


_TENSORFLOWSERVING = _descriptor.Descriptor(
  name='TensorFlowServing',
  full_name='tfx.components.infra_validator.TensorFlowServing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_name', full_name='tfx.components.infra_validator.TensorFlowServing.image_name', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='tfx.components.infra_validator.TensorFlowServing.tags', index=1,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digests', full_name='tfx.components.infra_validator.TensorFlowServing.digests', index=2,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=369,
  serialized_end=439,
)


_LOCALDOCKERCONFIG = _descriptor.Descriptor(
  name='LocalDockerConfig',
  full_name='tfx.components.infra_validator.LocalDockerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_base_url', full_name='tfx.components.infra_validator.LocalDockerConfig.client_base_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_api_version', full_name='tfx.components.infra_validator.LocalDockerConfig.client_api_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_timeout_seconds', full_name='tfx.components.infra_validator.LocalDockerConfig.client_timeout_seconds', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=441,
  serialized_end=545,
)


_KUBERNETESCONFIG = _descriptor.Descriptor(
  name='KubernetesConfig',
  full_name='tfx.components.infra_validator.KubernetesConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_account_name', full_name='tfx.components.infra_validator.KubernetesConfig.service_account_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_deadline_seconds', full_name='tfx.components.infra_validator.KubernetesConfig.active_deadline_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=547,
  serialized_end=628,
)


_VALIDATIONSPEC = _descriptor.Descriptor(
  name='ValidationSpec',
  full_name='tfx.components.infra_validator.ValidationSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_loading_time_seconds', full_name='tfx.components.infra_validator.ValidationSpec.max_loading_time_seconds', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_tries', full_name='tfx.components.infra_validator.ValidationSpec.num_tries', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=630,
  serialized_end=699,
)


_REQUESTSPEC = _descriptor.Descriptor(
  name='RequestSpec',
  full_name='tfx.components.infra_validator.RequestSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensorflow_serving', full_name='tfx.components.infra_validator.RequestSpec.tensorflow_serving', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='split_name', full_name='tfx.components.infra_validator.RequestSpec.split_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_examples', full_name='tfx.components.infra_validator.RequestSpec.num_examples', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='tfx.components.infra_validator.RequestSpec.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=702,
  serialized_end=857,
)


_TENSORFLOWSERVINGREQUESTSPEC = _descriptor.Descriptor(
  name='TensorFlowServingRequestSpec',
  full_name='tfx.components.infra_validator.TensorFlowServingRequestSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_set', full_name='tfx.components.infra_validator.TensorFlowServingRequestSpec.tag_set', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_names', full_name='tfx.components.infra_validator.TensorFlowServingRequestSpec.signature_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=859,
  serialized_end=931,
)

_SERVINGSPEC.fields_by_name['tensorflow_serving'].message_type = _TENSORFLOWSERVING
_SERVINGSPEC.fields_by_name['local_docker'].message_type = _LOCALDOCKERCONFIG
_SERVINGSPEC.fields_by_name['kubernetes'].message_type = _KUBERNETESCONFIG
_SERVINGSPEC.oneofs_by_name['serving_binary'].fields.append(
  _SERVINGSPEC.fields_by_name['tensorflow_serving'])
_SERVINGSPEC.fields_by_name['tensorflow_serving'].containing_oneof = _SERVINGSPEC.oneofs_by_name['serving_binary']
_SERVINGSPEC.oneofs_by_name['serving_platform'].fields.append(
  _SERVINGSPEC.fields_by_name['local_docker'])
_SERVINGSPEC.fields_by_name['local_docker'].containing_oneof = _SERVINGSPEC.oneofs_by_name['serving_platform']
_SERVINGSPEC.oneofs_by_name['serving_platform'].fields.append(
  _SERVINGSPEC.fields_by_name['kubernetes'])
_SERVINGSPEC.fields_by_name['kubernetes'].containing_oneof = _SERVINGSPEC.oneofs_by_name['serving_platform']
_REQUESTSPEC.fields_by_name['tensorflow_serving'].message_type = _TENSORFLOWSERVINGREQUESTSPEC
_REQUESTSPEC.oneofs_by_name['kind'].fields.append(
  _REQUESTSPEC.fields_by_name['tensorflow_serving'])
_REQUESTSPEC.fields_by_name['tensorflow_serving'].containing_oneof = _REQUESTSPEC.oneofs_by_name['kind']
DESCRIPTOR.message_types_by_name['ServingSpec'] = _SERVINGSPEC
DESCRIPTOR.message_types_by_name['TensorFlowServing'] = _TENSORFLOWSERVING
DESCRIPTOR.message_types_by_name['LocalDockerConfig'] = _LOCALDOCKERCONFIG
DESCRIPTOR.message_types_by_name['KubernetesConfig'] = _KUBERNETESCONFIG
DESCRIPTOR.message_types_by_name['ValidationSpec'] = _VALIDATIONSPEC
DESCRIPTOR.message_types_by_name['RequestSpec'] = _REQUESTSPEC
DESCRIPTOR.message_types_by_name['TensorFlowServingRequestSpec'] = _TENSORFLOWSERVINGREQUESTSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServingSpec = _reflection.GeneratedProtocolMessageType('ServingSpec', (_message.Message,), {
  'DESCRIPTOR' : _SERVINGSPEC,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.ServingSpec)
  })
_sym_db.RegisterMessage(ServingSpec)

TensorFlowServing = _reflection.GeneratedProtocolMessageType('TensorFlowServing', (_message.Message,), {
  'DESCRIPTOR' : _TENSORFLOWSERVING,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.TensorFlowServing)
  })
_sym_db.RegisterMessage(TensorFlowServing)

LocalDockerConfig = _reflection.GeneratedProtocolMessageType('LocalDockerConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOCALDOCKERCONFIG,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.LocalDockerConfig)
  })
_sym_db.RegisterMessage(LocalDockerConfig)

KubernetesConfig = _reflection.GeneratedProtocolMessageType('KubernetesConfig', (_message.Message,), {
  'DESCRIPTOR' : _KUBERNETESCONFIG,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.KubernetesConfig)
  })
_sym_db.RegisterMessage(KubernetesConfig)

ValidationSpec = _reflection.GeneratedProtocolMessageType('ValidationSpec', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONSPEC,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.ValidationSpec)
  })
_sym_db.RegisterMessage(ValidationSpec)

RequestSpec = _reflection.GeneratedProtocolMessageType('RequestSpec', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSPEC,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.RequestSpec)
  })
_sym_db.RegisterMessage(RequestSpec)

TensorFlowServingRequestSpec = _reflection.GeneratedProtocolMessageType('TensorFlowServingRequestSpec', (_message.Message,), {
  'DESCRIPTOR' : _TENSORFLOWSERVINGREQUESTSPEC,
  '__module__' : 'tfx.proto.infra_validator_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.infra_validator.TensorFlowServingRequestSpec)
  })
_sym_db.RegisterMessage(TensorFlowServingRequestSpec)


# @@protoc_insertion_point(module_scope)
