# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riva/proto/riva_nlp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19riva/proto/riva_nlp.proto\x12\x0fnvidia.riva.nlp\";\n\x0eNLPModelParams\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"c\n\x14TextTransformRequest\x12\x0c\n\x04text\x18\x01 \x03(\t\x12\r\n\x05top_n\x18\x02 \x01(\r\x12.\n\x05model\x18\x03 \x01(\x0b\x32\x1f.nvidia.riva.nlp.NLPModelParams\"%\n\x15TextTransformResponse\x12\x0c\n\x04text\x18\x01 \x03(\t\"_\n\x10TextClassRequest\x12\x0c\n\x04text\x18\x01 \x03(\t\x12\r\n\x05top_n\x18\x02 \x01(\r\x12.\n\x05model\x18\x03 \x01(\x0b\x32\x1f.nvidia.riva.nlp.NLPModelParams\"3\n\x0e\x43lassification\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"\"\n\x04Span\x12\r\n\x05start\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\"G\n\x14\x43lassificationResult\x12/\n\x06labels\x18\x01 \x03(\x0b\x32\x1f.nvidia.riva.nlp.Classification\"K\n\x11TextClassResponse\x12\x36\n\x07results\x18\x01 \x03(\x0b\x32%.nvidia.riva.nlp.ClassificationResult\"`\n\x11TokenClassRequest\x12\x0c\n\x04text\x18\x01 \x03(\t\x12\r\n\x05top_n\x18\x03 \x01(\r\x12.\n\x05model\x18\x04 \x01(\x0b\x32\x1f.nvidia.riva.nlp.NLPModelParams\"u\n\x0fTokenClassValue\x12\r\n\x05token\x18\x01 \x01(\t\x12.\n\x05label\x18\x02 \x03(\x0b\x32\x1f.nvidia.riva.nlp.Classification\x12#\n\x04span\x18\x03 \x03(\x0b\x32\x15.nvidia.riva.nlp.Span\"G\n\x12TokenClassSequence\x12\x31\n\x07results\x18\x01 \x03(\x0b\x32 .nvidia.riva.nlp.TokenClassValue\"J\n\x12TokenClassResponse\x12\x34\n\x07results\x18\x01 \x03(\x0b\x32#.nvidia.riva.nlp.TokenClassSequence\"\x16\n\x14\x41nalyzeIntentContext\"\x94\x01\n\x14\x41nalyzeIntentOptions\x12\x19\n\x0fprevious_intent\x18\x01 \x01(\tH\x00\x12\x38\n\x07vectors\x18\x02 \x01(\x0b\x32%.nvidia.riva.nlp.AnalyzeIntentContextH\x00\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0c\n\x04lang\x18\x04 \x01(\tB\t\n\x07\x63ontext\"]\n\x14\x41nalyzeIntentRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x36\n\x07options\x18\x02 \x01(\x0b\x32%.nvidia.riva.nlp.AnalyzeIntentOptions\"\xbe\x01\n\x15\x41nalyzeIntentResponse\x12/\n\x06intent\x18\x01 \x01(\x0b\x32\x1f.nvidia.riva.nlp.Classification\x12/\n\x05slots\x18\x02 \x03(\x0b\x32 .nvidia.riva.nlp.TokenClassValue\x12\x12\n\ndomain_str\x18\x03 \x01(\t\x12/\n\x06\x64omain\x18\x04 \x01(\x0b\x32\x1f.nvidia.riva.nlp.Classification\"&\n\x16\x41nalyzeEntitiesOptions\x12\x0c\n\x04lang\x18\x04 \x01(\t\"a\n\x16\x41nalyzeEntitiesRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x38\n\x07options\x18\x02 \x01(\x0b\x32\'.nvidia.riva.nlp.AnalyzeEntitiesOptions\"D\n\x13NaturalQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\r\n\x05top_n\x18\x02 \x01(\r\x12\x0f\n\x07\x63ontext\x18\x03 \x01(\t\"3\n\x12NaturalQueryResult\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"L\n\x14NaturalQueryResponse\x12\x34\n\x07results\x18\x01 \x03(\x0b\x32#.nvidia.riva.nlp.NaturalQueryResult2\xb9\x05\n\x19RivaLanguageUnderstanding\x12W\n\x0c\x43lassifyText\x12!.nvidia.riva.nlp.TextClassRequest\x1a\".nvidia.riva.nlp.TextClassResponse\"\x00\x12[\n\x0e\x43lassifyTokens\x12\".nvidia.riva.nlp.TokenClassRequest\x1a#.nvidia.riva.nlp.TokenClassResponse\"\x00\x12`\n\rTransformText\x12%.nvidia.riva.nlp.TextTransformRequest\x1a&.nvidia.riva.nlp.TextTransformResponse\"\x00\x12\x61\n\x0f\x41nalyzeEntities\x12\'.nvidia.riva.nlp.AnalyzeEntitiesRequest\x1a#.nvidia.riva.nlp.TokenClassResponse\"\x00\x12`\n\rAnalyzeIntent\x12%.nvidia.riva.nlp.AnalyzeIntentRequest\x1a&.nvidia.riva.nlp.AnalyzeIntentResponse\"\x00\x12`\n\rPunctuateText\x12%.nvidia.riva.nlp.TextTransformRequest\x1a&.nvidia.riva.nlp.TextTransformResponse\"\x00\x12]\n\x0cNaturalQuery\x12$.nvidia.riva.nlp.NaturalQueryRequest\x1a%.nvidia.riva.nlp.NaturalQueryResponse\"\x00\x42\x1bZ\x16nvidia.com/riva_speech\xf8\x01\x01\x62\x06proto3')



_NLPMODELPARAMS = DESCRIPTOR.message_types_by_name['NLPModelParams']
_TEXTTRANSFORMREQUEST = DESCRIPTOR.message_types_by_name['TextTransformRequest']
_TEXTTRANSFORMRESPONSE = DESCRIPTOR.message_types_by_name['TextTransformResponse']
_TEXTCLASSREQUEST = DESCRIPTOR.message_types_by_name['TextClassRequest']
_CLASSIFICATION = DESCRIPTOR.message_types_by_name['Classification']
_SPAN = DESCRIPTOR.message_types_by_name['Span']
_CLASSIFICATIONRESULT = DESCRIPTOR.message_types_by_name['ClassificationResult']
_TEXTCLASSRESPONSE = DESCRIPTOR.message_types_by_name['TextClassResponse']
_TOKENCLASSREQUEST = DESCRIPTOR.message_types_by_name['TokenClassRequest']
_TOKENCLASSVALUE = DESCRIPTOR.message_types_by_name['TokenClassValue']
_TOKENCLASSSEQUENCE = DESCRIPTOR.message_types_by_name['TokenClassSequence']
_TOKENCLASSRESPONSE = DESCRIPTOR.message_types_by_name['TokenClassResponse']
_ANALYZEINTENTCONTEXT = DESCRIPTOR.message_types_by_name['AnalyzeIntentContext']
_ANALYZEINTENTOPTIONS = DESCRIPTOR.message_types_by_name['AnalyzeIntentOptions']
_ANALYZEINTENTREQUEST = DESCRIPTOR.message_types_by_name['AnalyzeIntentRequest']
_ANALYZEINTENTRESPONSE = DESCRIPTOR.message_types_by_name['AnalyzeIntentResponse']
_ANALYZEENTITIESOPTIONS = DESCRIPTOR.message_types_by_name['AnalyzeEntitiesOptions']
_ANALYZEENTITIESREQUEST = DESCRIPTOR.message_types_by_name['AnalyzeEntitiesRequest']
_NATURALQUERYREQUEST = DESCRIPTOR.message_types_by_name['NaturalQueryRequest']
_NATURALQUERYRESULT = DESCRIPTOR.message_types_by_name['NaturalQueryResult']
_NATURALQUERYRESPONSE = DESCRIPTOR.message_types_by_name['NaturalQueryResponse']
NLPModelParams = _reflection.GeneratedProtocolMessageType('NLPModelParams', (_message.Message,), {
  'DESCRIPTOR' : _NLPMODELPARAMS,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.NLPModelParams)
  })
_sym_db.RegisterMessage(NLPModelParams)

TextTransformRequest = _reflection.GeneratedProtocolMessageType('TextTransformRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEXTTRANSFORMREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TextTransformRequest)
  })
_sym_db.RegisterMessage(TextTransformRequest)

TextTransformResponse = _reflection.GeneratedProtocolMessageType('TextTransformResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEXTTRANSFORMRESPONSE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TextTransformResponse)
  })
_sym_db.RegisterMessage(TextTransformResponse)

TextClassRequest = _reflection.GeneratedProtocolMessageType('TextClassRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEXTCLASSREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TextClassRequest)
  })
_sym_db.RegisterMessage(TextClassRequest)

Classification = _reflection.GeneratedProtocolMessageType('Classification', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATION,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.Classification)
  })
_sym_db.RegisterMessage(Classification)

Span = _reflection.GeneratedProtocolMessageType('Span', (_message.Message,), {
  'DESCRIPTOR' : _SPAN,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.Span)
  })
_sym_db.RegisterMessage(Span)

ClassificationResult = _reflection.GeneratedProtocolMessageType('ClassificationResult', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONRESULT,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.ClassificationResult)
  })
_sym_db.RegisterMessage(ClassificationResult)

TextClassResponse = _reflection.GeneratedProtocolMessageType('TextClassResponse', (_message.Message,), {
  'DESCRIPTOR' : _TEXTCLASSRESPONSE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TextClassResponse)
  })
_sym_db.RegisterMessage(TextClassResponse)

TokenClassRequest = _reflection.GeneratedProtocolMessageType('TokenClassRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCLASSREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TokenClassRequest)
  })
_sym_db.RegisterMessage(TokenClassRequest)

TokenClassValue = _reflection.GeneratedProtocolMessageType('TokenClassValue', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCLASSVALUE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TokenClassValue)
  })
_sym_db.RegisterMessage(TokenClassValue)

TokenClassSequence = _reflection.GeneratedProtocolMessageType('TokenClassSequence', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCLASSSEQUENCE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TokenClassSequence)
  })
_sym_db.RegisterMessage(TokenClassSequence)

TokenClassResponse = _reflection.GeneratedProtocolMessageType('TokenClassResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENCLASSRESPONSE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.TokenClassResponse)
  })
_sym_db.RegisterMessage(TokenClassResponse)

AnalyzeIntentContext = _reflection.GeneratedProtocolMessageType('AnalyzeIntentContext', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEINTENTCONTEXT,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeIntentContext)
  })
_sym_db.RegisterMessage(AnalyzeIntentContext)

AnalyzeIntentOptions = _reflection.GeneratedProtocolMessageType('AnalyzeIntentOptions', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEINTENTOPTIONS,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeIntentOptions)
  })
_sym_db.RegisterMessage(AnalyzeIntentOptions)

AnalyzeIntentRequest = _reflection.GeneratedProtocolMessageType('AnalyzeIntentRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEINTENTREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeIntentRequest)
  })
_sym_db.RegisterMessage(AnalyzeIntentRequest)

AnalyzeIntentResponse = _reflection.GeneratedProtocolMessageType('AnalyzeIntentResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEINTENTRESPONSE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeIntentResponse)
  })
_sym_db.RegisterMessage(AnalyzeIntentResponse)

AnalyzeEntitiesOptions = _reflection.GeneratedProtocolMessageType('AnalyzeEntitiesOptions', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEENTITIESOPTIONS,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeEntitiesOptions)
  })
_sym_db.RegisterMessage(AnalyzeEntitiesOptions)

AnalyzeEntitiesRequest = _reflection.GeneratedProtocolMessageType('AnalyzeEntitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEENTITIESREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.AnalyzeEntitiesRequest)
  })
_sym_db.RegisterMessage(AnalyzeEntitiesRequest)

NaturalQueryRequest = _reflection.GeneratedProtocolMessageType('NaturalQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _NATURALQUERYREQUEST,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.NaturalQueryRequest)
  })
_sym_db.RegisterMessage(NaturalQueryRequest)

NaturalQueryResult = _reflection.GeneratedProtocolMessageType('NaturalQueryResult', (_message.Message,), {
  'DESCRIPTOR' : _NATURALQUERYRESULT,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.NaturalQueryResult)
  })
_sym_db.RegisterMessage(NaturalQueryResult)

NaturalQueryResponse = _reflection.GeneratedProtocolMessageType('NaturalQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _NATURALQUERYRESPONSE,
  '__module__' : 'riva.proto.riva_nlp_pb2'
  # @@protoc_insertion_point(class_scope:nvidia.riva.nlp.NaturalQueryResponse)
  })
_sym_db.RegisterMessage(NaturalQueryResponse)

_RIVALANGUAGEUNDERSTANDING = DESCRIPTOR.services_by_name['RivaLanguageUnderstanding']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026nvidia.com/riva_speech\370\001\001'
  _NLPMODELPARAMS._serialized_start=46
  _NLPMODELPARAMS._serialized_end=105
  _TEXTTRANSFORMREQUEST._serialized_start=107
  _TEXTTRANSFORMREQUEST._serialized_end=206
  _TEXTTRANSFORMRESPONSE._serialized_start=208
  _TEXTTRANSFORMRESPONSE._serialized_end=245
  _TEXTCLASSREQUEST._serialized_start=247
  _TEXTCLASSREQUEST._serialized_end=342
  _CLASSIFICATION._serialized_start=344
  _CLASSIFICATION._serialized_end=395
  _SPAN._serialized_start=397
  _SPAN._serialized_end=431
  _CLASSIFICATIONRESULT._serialized_start=433
  _CLASSIFICATIONRESULT._serialized_end=504
  _TEXTCLASSRESPONSE._serialized_start=506
  _TEXTCLASSRESPONSE._serialized_end=581
  _TOKENCLASSREQUEST._serialized_start=583
  _TOKENCLASSREQUEST._serialized_end=679
  _TOKENCLASSVALUE._serialized_start=681
  _TOKENCLASSVALUE._serialized_end=798
  _TOKENCLASSSEQUENCE._serialized_start=800
  _TOKENCLASSSEQUENCE._serialized_end=871
  _TOKENCLASSRESPONSE._serialized_start=873
  _TOKENCLASSRESPONSE._serialized_end=947
  _ANALYZEINTENTCONTEXT._serialized_start=949
  _ANALYZEINTENTCONTEXT._serialized_end=971
  _ANALYZEINTENTOPTIONS._serialized_start=974
  _ANALYZEINTENTOPTIONS._serialized_end=1122
  _ANALYZEINTENTREQUEST._serialized_start=1124
  _ANALYZEINTENTREQUEST._serialized_end=1217
  _ANALYZEINTENTRESPONSE._serialized_start=1220
  _ANALYZEINTENTRESPONSE._serialized_end=1410
  _ANALYZEENTITIESOPTIONS._serialized_start=1412
  _ANALYZEENTITIESOPTIONS._serialized_end=1450
  _ANALYZEENTITIESREQUEST._serialized_start=1452
  _ANALYZEENTITIESREQUEST._serialized_end=1549
  _NATURALQUERYREQUEST._serialized_start=1551
  _NATURALQUERYREQUEST._serialized_end=1619
  _NATURALQUERYRESULT._serialized_start=1621
  _NATURALQUERYRESULT._serialized_end=1672
  _NATURALQUERYRESPONSE._serialized_start=1674
  _NATURALQUERYRESPONSE._serialized_end=1750
  _RIVALANGUAGEUNDERSTANDING._serialized_start=1753
  _RIVALANGUAGEUNDERSTANDING._serialized_end=2450
# @@protoc_insertion_point(module_scope)
