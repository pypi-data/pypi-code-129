# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: th2_grpc_act_template/act_template.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from th2_grpc_common import common_pb2 as th2__grpc__common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='th2_grpc_act_template/act_template.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\031com.exactpro.th2.act.grpcP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(th2_grpc_act_template/act_template.proto\x1a\x1cth2_grpc_common/common.proto\"\x19\n\x07Symbols\x12\x0e\n\x06symbol\x18\x01 \x03(\t\"Y\n\x13SendMessageResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x02 \x01(\x0b\x32\x0b.Checkpoint\"\x92\x01\n\x13PlaceMessageRequest\x12\x19\n\x07message\x18\x01 \x01(\x0b\x32\x08.Message\x12(\n\rconnection_id\x18\x02 \x01(\x0b\x32\r.ConnectionIDB\x02\x18\x01\x12!\n\x0fparent_event_id\x18\x04 \x01(\x0b\x32\x08.EventID\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"~\n\x14PlaceMessageResponse\x12\"\n\x10response_message\x18\x01 \x01(\x0b\x32\x08.Message\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x03 \x01(\x0b\x32\x0b.Checkpoint\"\x86\x01\n\x1cPlaceMessageMultipleResponse\x12\"\n\x10response_message\x18\x01 \x03(\x0b\x32\x08.Message\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x03 \x01(\x0b\x32\x0b.Checkpoint\"\x80\x02\n\x19PlaceSecurityListResponse\x12V\n\x16securityListDictionary\x18\x01 \x03(\x0b\x32\x36.PlaceSecurityListResponse.SecurityListDictionaryEntry\x12\x1e\n\x06status\x18\x02 \x01(\x0b\x32\x0e.RequestStatus\x12\"\n\rcheckpoint_id\x18\x03 \x01(\x0b\x32\x0b.Checkpoint\x1aG\n\x1bSecurityListDictionaryEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x17\n\x05value\x18\x02 \x01(\x0b\x32\x08.Symbols:\x02\x38\x01\x32\x84\x05\n\x03\x41\x63t\x12\x34\n\rplaceOrderFIX\x12\x14.PlaceMessageRequest\x1a\x0b.Checkpoint\"\x00\x12;\n\x0bsendMessage\x12\x14.PlaceMessageRequest\x1a\x14.SendMessageResponse\"\x00\x12\x45\n\x14placeQuoteRequestFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12\x46\n\rplaceQuoteFIX\x12\x14.PlaceMessageRequest\x1a\x1d.PlaceMessageMultipleResponse\"\x00\x12O\n\x1eplaceOrderMassCancelRequestFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12\x44\n\x13placeQuoteCancelFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12\x46\n\x15placeQuoteResponseFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12L\n\x1bplaceSecurityListRequestFIX\x12\x14.PlaceMessageRequest\x1a\x15.PlaceMessageResponse\"\x00\x12N\n\x18placeSecurityListRequest\x12\x14.PlaceMessageRequest\x1a\x1a.PlaceSecurityListResponse\"\x00\x42\x1d\n\x19\x63om.exactpro.th2.act.grpcP\x01\x62\x06proto3'
  ,
  dependencies=[th2__grpc__common_dot_common__pb2.DESCRIPTOR,])




_SYMBOLS = _descriptor.Descriptor(
  name='Symbols',
  full_name='Symbols',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='Symbols.symbol', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=74,
  serialized_end=99,
)


_SENDMESSAGERESPONSE = _descriptor.Descriptor(
  name='SendMessageResponse',
  full_name='SendMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SendMessageResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkpoint_id', full_name='SendMessageResponse.checkpoint_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=101,
  serialized_end=190,
)


_PLACEMESSAGEREQUEST = _descriptor.Descriptor(
  name='PlaceMessageRequest',
  full_name='PlaceMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='PlaceMessageRequest.message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='PlaceMessageRequest.connection_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_event_id', full_name='PlaceMessageRequest.parent_event_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PlaceMessageRequest.description', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=193,
  serialized_end=339,
)


_PLACEMESSAGERESPONSE = _descriptor.Descriptor(
  name='PlaceMessageResponse',
  full_name='PlaceMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_message', full_name='PlaceMessageResponse.response_message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='PlaceMessageResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkpoint_id', full_name='PlaceMessageResponse.checkpoint_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=341,
  serialized_end=467,
)


_PLACEMESSAGEMULTIPLERESPONSE = _descriptor.Descriptor(
  name='PlaceMessageMultipleResponse',
  full_name='PlaceMessageMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_message', full_name='PlaceMessageMultipleResponse.response_message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='PlaceMessageMultipleResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkpoint_id', full_name='PlaceMessageMultipleResponse.checkpoint_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=470,
  serialized_end=604,
)


_PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY = _descriptor.Descriptor(
  name='SecurityListDictionaryEntry',
  full_name='PlaceSecurityListResponse.SecurityListDictionaryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PlaceSecurityListResponse.SecurityListDictionaryEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PlaceSecurityListResponse.SecurityListDictionaryEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=863,
)

_PLACESECURITYLISTRESPONSE = _descriptor.Descriptor(
  name='PlaceSecurityListResponse',
  full_name='PlaceSecurityListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='securityListDictionary', full_name='PlaceSecurityListResponse.securityListDictionary', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='PlaceSecurityListResponse.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkpoint_id', full_name='PlaceSecurityListResponse.checkpoint_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=863,
)

_SENDMESSAGERESPONSE.fields_by_name['status'].message_type = th2__grpc__common_dot_common__pb2._REQUESTSTATUS
_SENDMESSAGERESPONSE.fields_by_name['checkpoint_id'].message_type = th2__grpc__common_dot_common__pb2._CHECKPOINT
_PLACEMESSAGEREQUEST.fields_by_name['message'].message_type = th2__grpc__common_dot_common__pb2._MESSAGE
_PLACEMESSAGEREQUEST.fields_by_name['connection_id'].message_type = th2__grpc__common_dot_common__pb2._CONNECTIONID
_PLACEMESSAGEREQUEST.fields_by_name['parent_event_id'].message_type = th2__grpc__common_dot_common__pb2._EVENTID
_PLACEMESSAGERESPONSE.fields_by_name['response_message'].message_type = th2__grpc__common_dot_common__pb2._MESSAGE
_PLACEMESSAGERESPONSE.fields_by_name['status'].message_type = th2__grpc__common_dot_common__pb2._REQUESTSTATUS
_PLACEMESSAGERESPONSE.fields_by_name['checkpoint_id'].message_type = th2__grpc__common_dot_common__pb2._CHECKPOINT
_PLACEMESSAGEMULTIPLERESPONSE.fields_by_name['response_message'].message_type = th2__grpc__common_dot_common__pb2._MESSAGE
_PLACEMESSAGEMULTIPLERESPONSE.fields_by_name['status'].message_type = th2__grpc__common_dot_common__pb2._REQUESTSTATUS
_PLACEMESSAGEMULTIPLERESPONSE.fields_by_name['checkpoint_id'].message_type = th2__grpc__common_dot_common__pb2._CHECKPOINT
_PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY.fields_by_name['value'].message_type = _SYMBOLS
_PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY.containing_type = _PLACESECURITYLISTRESPONSE
_PLACESECURITYLISTRESPONSE.fields_by_name['securityListDictionary'].message_type = _PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY
_PLACESECURITYLISTRESPONSE.fields_by_name['status'].message_type = th2__grpc__common_dot_common__pb2._REQUESTSTATUS
_PLACESECURITYLISTRESPONSE.fields_by_name['checkpoint_id'].message_type = th2__grpc__common_dot_common__pb2._CHECKPOINT
DESCRIPTOR.message_types_by_name['Symbols'] = _SYMBOLS
DESCRIPTOR.message_types_by_name['SendMessageResponse'] = _SENDMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['PlaceMessageRequest'] = _PLACEMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['PlaceMessageResponse'] = _PLACEMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['PlaceMessageMultipleResponse'] = _PLACEMESSAGEMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['PlaceSecurityListResponse'] = _PLACESECURITYLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Symbols = _reflection.GeneratedProtocolMessageType('Symbols', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOLS,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:Symbols)
  })
_sym_db.RegisterMessage(Symbols)

SendMessageResponse = _reflection.GeneratedProtocolMessageType('SendMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGERESPONSE,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:SendMessageResponse)
  })
_sym_db.RegisterMessage(SendMessageResponse)

PlaceMessageRequest = _reflection.GeneratedProtocolMessageType('PlaceMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLACEMESSAGEREQUEST,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:PlaceMessageRequest)
  })
_sym_db.RegisterMessage(PlaceMessageRequest)

PlaceMessageResponse = _reflection.GeneratedProtocolMessageType('PlaceMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLACEMESSAGERESPONSE,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:PlaceMessageResponse)
  })
_sym_db.RegisterMessage(PlaceMessageResponse)

PlaceMessageMultipleResponse = _reflection.GeneratedProtocolMessageType('PlaceMessageMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLACEMESSAGEMULTIPLERESPONSE,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:PlaceMessageMultipleResponse)
  })
_sym_db.RegisterMessage(PlaceMessageMultipleResponse)

PlaceSecurityListResponse = _reflection.GeneratedProtocolMessageType('PlaceSecurityListResponse', (_message.Message,), {

  'SecurityListDictionaryEntry' : _reflection.GeneratedProtocolMessageType('SecurityListDictionaryEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY,
    '__module__' : 'th2_grpc_act_template.act_template_pb2'
    # @@protoc_insertion_point(class_scope:PlaceSecurityListResponse.SecurityListDictionaryEntry)
    })
  ,
  'DESCRIPTOR' : _PLACESECURITYLISTRESPONSE,
  '__module__' : 'th2_grpc_act_template.act_template_pb2'
  # @@protoc_insertion_point(class_scope:PlaceSecurityListResponse)
  })
_sym_db.RegisterMessage(PlaceSecurityListResponse)
_sym_db.RegisterMessage(PlaceSecurityListResponse.SecurityListDictionaryEntry)


DESCRIPTOR._options = None
_PLACEMESSAGEREQUEST.fields_by_name['connection_id']._options = None
_PLACESECURITYLISTRESPONSE_SECURITYLISTDICTIONARYENTRY._options = None

_ACT = _descriptor.ServiceDescriptor(
  name='Act',
  full_name='Act',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=866,
  serialized_end=1510,
  methods=[
  _descriptor.MethodDescriptor(
    name='placeOrderFIX',
    full_name='Act.placeOrderFIX',
    index=0,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=th2__grpc__common_dot_common__pb2._CHECKPOINT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendMessage',
    full_name='Act.sendMessage',
    index=1,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_SENDMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeQuoteRequestFIX',
    full_name='Act.placeQuoteRequestFIX',
    index=2,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeQuoteFIX',
    full_name='Act.placeQuoteFIX',
    index=3,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGEMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeOrderMassCancelRequestFIX',
    full_name='Act.placeOrderMassCancelRequestFIX',
    index=4,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeQuoteCancelFIX',
    full_name='Act.placeQuoteCancelFIX',
    index=5,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeQuoteResponseFIX',
    full_name='Act.placeQuoteResponseFIX',
    index=6,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeSecurityListRequestFIX',
    full_name='Act.placeSecurityListRequestFIX',
    index=7,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACEMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='placeSecurityListRequest',
    full_name='Act.placeSecurityListRequest',
    index=8,
    containing_service=None,
    input_type=_PLACEMESSAGEREQUEST,
    output_type=_PLACESECURITYLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACT)

DESCRIPTOR.services_by_name['Act'] = _ACT

# @@protoc_insertion_point(module_scope)
