# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/value/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api.value import query_filter_pb2 as api_dot_value_dot_query__filter__pb2
from layerapi.api.value import query_pagination_pb2 as api_dot_value_dot_query__pagination__pb2
from layerapi.api.value import query_sort_pb2 as api_dot_value_dot_query__sort__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/value/query.proto\x12\x03\x61pi\x1a\x1c\x61pi/value/query_filter.proto\x1a api/value/query_pagination.proto\x1a\x1a\x61pi/value/query_sort.proto\"\x7f\n\x1aSimpleFilterSortPagination\x12\x1c\n\x07\x66ilters\x18\x01 \x03(\x0b\x32\x0b.api.Filter\x12\x18\n\x05sorts\x18\x02 \x03(\x0b\x32\t.api.Sort\x12)\n\npagination\x18\x03 \x01(\x0b\x32\x15.api.SimplePaginationB\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_SIMPLEFILTERSORTPAGINATION = DESCRIPTOR.message_types_by_name['SimpleFilterSortPagination']
SimpleFilterSortPagination = _reflection.GeneratedProtocolMessageType('SimpleFilterSortPagination', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEFILTERSORTPAGINATION,
  '__module__' : 'api.value.query_pb2'
  # @@protoc_insertion_point(class_scope:api.SimpleFilterSortPagination)
  })
_sym_db.RegisterMessage(SimpleFilterSortPagination)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _SIMPLEFILTERSORTPAGINATION._serialized_start=122
  _SIMPLEFILTERSORTPAGINATION._serialized_end=249
# @@protoc_insertion_point(module_scope)
