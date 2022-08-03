# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/entity/dataset_build.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from layerapi.api import ids_pb2 as api_dot_ids__pb2
from layerapi.api.value import dataset_stats_pb2 as api_dot_value_dot_dataset__stats__pb2
from layerapi.api.value import storage_location_pb2 as api_dot_value_dot_storage__location__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/entity/dataset_build.proto\x12\x03\x61pi\x1a\rapi/ids.proto\x1a\x1d\x61pi/value/dataset_stats.proto\x1a api/value/storage_location.proto\"\xd2\t\n\x0c\x44\x61tasetBuild\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.api.DatasetBuildId\x12\x31\n\x12\x64\x61taset_version_id\x18\x02 \x01(\x0b\x32\x15.api.DatasetVersionId\x12\r\n\x05index\x18\x03 \x01(\x03\x12&\n\x08location\x18\x04 \x01(\x0b\x32\x14.api.StorageLocation\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\"\n\rcreated_by_id\x18\x06 \x01(\x0b\x32\x0b.api.UserId\x12\x17\n\x0fstart_timestamp\x18\x07 \x01(\x03\x12\x15\n\rend_timestamp\x18\x08 \x01(\x03\x12\x35\n\nbuild_info\x18\t \x01(\x0b\x32!.api.DatasetBuild.BuildStatusInfo\x12/\n\nbuild_type\x18\n \x01(\x0e\x32\x1b.api.DatasetBuild.BuildType\x12\x39\n\x0f\x64\x65ployment_info\x18\x0b \x01(\x0b\x32 .api.DatasetBuild.DeploymentInfo\x12<\n\x11\x62uild_entity_type\x18\r \x01(\x0e\x32!.api.DatasetBuild.BuildEntityType\x12 \n\x05stats\x18\x0e \x01(\x0b\x32\x11.api.DatasetStats\x12\"\n\ndataset_id\x18\x0f \x01(\x0b\x32\x0e.api.DatasetId\x12\x0e\n\x06\x66\x61\x62ric\x18\x10 \x01(\t\x1aN\n\x0f\x42uildStatusInfo\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.api.DatasetBuild.BuildStatus\x12\x0c\n\x04info\x18\x03 \x01(\t\x1aW\n\x0e\x44\x65ploymentInfo\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".api.DatasetBuild.DeploymentStatus\x12\x11\n\ttimestamp\x18\x02 \x01(\x06\"T\n\tBuildType\x12\x16\n\x12\x42UILD_TYPE_INVALID\x10\x00\x12\x15\n\x11\x42UILD_TYPE_AD_HOC\x10\x01\x12\x18\n\x14\x42UILD_TYPE_SCHEDULED\x10\x02\"\xae\x01\n\x0b\x42uildStatus\x12\x18\n\x14\x42UILD_STATUS_INVALID\x10\x00\x12\x18\n\x14\x42UILD_STATUS_STARTED\x10\x01\x12\x1a\n\x16\x42UILD_STATUS_COMPLETED\x10\x02\x12\x17\n\x13\x42UILD_STATUS_FAILED\x10\x03\x12\x1c\n\x18\x42UILD_STATUS_NOT_STARTED\x10\x04\x12\x18\n\x14\x42UILD_STATUS_UNKNOWN\x10\x05\"\x95\x01\n\x10\x44\x65ploymentStatus\x12\x1d\n\x19\x44\x45PLOYMENT_STATUS_INVALID\x10\x00\x12\x1e\n\x1a\x44\x45PLOYMENT_STATUS_DEPLOYED\x10\x01\x12!\n\x1d\x44\x45PLOYMENT_STATUS_NONDEPLOYED\x10\x02\x12\x1f\n\x1b\x44\x45PLOYMENT_STATUS_DEPLOYING\x10\x03\"O\n\x0f\x42uildEntityType\x12\x1d\n\x19\x42UILD_ENTITY_TYPE_INVALID\x10\x00\x12\x1d\n\x19\x42UILD_ENTITY_TYPE_DATASET\x10\x01\x42\x11\n\rcom.layer.apiP\x01\x62\x06proto3')



_DATASETBUILD = DESCRIPTOR.message_types_by_name['DatasetBuild']
_DATASETBUILD_BUILDSTATUSINFO = _DATASETBUILD.nested_types_by_name['BuildStatusInfo']
_DATASETBUILD_DEPLOYMENTINFO = _DATASETBUILD.nested_types_by_name['DeploymentInfo']
_DATASETBUILD_BUILDTYPE = _DATASETBUILD.enum_types_by_name['BuildType']
_DATASETBUILD_BUILDSTATUS = _DATASETBUILD.enum_types_by_name['BuildStatus']
_DATASETBUILD_DEPLOYMENTSTATUS = _DATASETBUILD.enum_types_by_name['DeploymentStatus']
_DATASETBUILD_BUILDENTITYTYPE = _DATASETBUILD.enum_types_by_name['BuildEntityType']
DatasetBuild = _reflection.GeneratedProtocolMessageType('DatasetBuild', (_message.Message,), {

  'BuildStatusInfo' : _reflection.GeneratedProtocolMessageType('BuildStatusInfo', (_message.Message,), {
    'DESCRIPTOR' : _DATASETBUILD_BUILDSTATUSINFO,
    '__module__' : 'api.entity.dataset_build_pb2'
    # @@protoc_insertion_point(class_scope:api.DatasetBuild.BuildStatusInfo)
    })
  ,

  'DeploymentInfo' : _reflection.GeneratedProtocolMessageType('DeploymentInfo', (_message.Message,), {
    'DESCRIPTOR' : _DATASETBUILD_DEPLOYMENTINFO,
    '__module__' : 'api.entity.dataset_build_pb2'
    # @@protoc_insertion_point(class_scope:api.DatasetBuild.DeploymentInfo)
    })
  ,
  'DESCRIPTOR' : _DATASETBUILD,
  '__module__' : 'api.entity.dataset_build_pb2'
  # @@protoc_insertion_point(class_scope:api.DatasetBuild)
  })
_sym_db.RegisterMessage(DatasetBuild)
_sym_db.RegisterMessage(DatasetBuild.BuildStatusInfo)
_sym_db.RegisterMessage(DatasetBuild.DeploymentInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.layer.apiP\001'
  _DATASETBUILD._serialized_start=120
  _DATASETBUILD._serialized_end=1354
  _DATASETBUILD_BUILDSTATUSINFO._serialized_start=691
  _DATASETBUILD_BUILDSTATUSINFO._serialized_end=769
  _DATASETBUILD_DEPLOYMENTINFO._serialized_start=771
  _DATASETBUILD_DEPLOYMENTINFO._serialized_end=858
  _DATASETBUILD_BUILDTYPE._serialized_start=860
  _DATASETBUILD_BUILDTYPE._serialized_end=944
  _DATASETBUILD_BUILDSTATUS._serialized_start=947
  _DATASETBUILD_BUILDSTATUS._serialized_end=1121
  _DATASETBUILD_DEPLOYMENTSTATUS._serialized_start=1124
  _DATASETBUILD_DEPLOYMENTSTATUS._serialized_end=1273
  _DATASETBUILD_BUILDENTITYTYPE._serialized_start=1275
  _DATASETBUILD_BUILDENTITYTYPE._serialized_end=1354
# @@protoc_insertion_point(module_scope)
