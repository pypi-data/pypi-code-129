# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/gov/v1beta1/genesis.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\"\x8f\x04\n\x0cGenesisState\x12=\n\x14starting_proposal_id\x18\x01 \x01(\x04\x42\x1f\xf2\xde\x1f\x1byaml:\"starting_proposal_id\"\x12?\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x10\xaa\xdf\x1f\x08\x44\x65posits\xc8\xde\x1f\x00\x12\x36\n\x05votes\x18\x03 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\r\xaa\xdf\x1f\x05Votes\xc8\xde\x1f\x00\x12\x42\n\tproposals\x18\x04 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x11\xaa\xdf\x1f\tProposals\xc8\xde\x1f\x00\x12X\n\x0e\x64\x65posit_params\x18\x05 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"deposit_params\"\x12U\n\rvoting_params\x18\x06 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:\"voting_params\"\x12R\n\x0ctally_params\x18\x07 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:\"tally_params\"B*Z(github.com/cosmos/cosmos-sdk/x/gov/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.gov.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/x/gov/types'
  _GENESISSTATE.fields_by_name['starting_proposal_id']._options = None
  _GENESISSTATE.fields_by_name['starting_proposal_id']._serialized_options = b'\362\336\037\033yaml:\"starting_proposal_id\"'
  _GENESISSTATE.fields_by_name['deposits']._options = None
  _GENESISSTATE.fields_by_name['deposits']._serialized_options = b'\252\337\037\010Deposits\310\336\037\000'
  _GENESISSTATE.fields_by_name['votes']._options = None
  _GENESISSTATE.fields_by_name['votes']._serialized_options = b'\252\337\037\005Votes\310\336\037\000'
  _GENESISSTATE.fields_by_name['proposals']._options = None
  _GENESISSTATE.fields_by_name['proposals']._serialized_options = b'\252\337\037\tProposals\310\336\037\000'
  _GENESISSTATE.fields_by_name['deposit_params']._options = None
  _GENESISSTATE.fields_by_name['deposit_params']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"deposit_params\"'
  _GENESISSTATE.fields_by_name['voting_params']._options = None
  _GENESISSTATE.fields_by_name['voting_params']._serialized_options = b'\310\336\037\000\362\336\037\024yaml:\"voting_params\"'
  _GENESISSTATE.fields_by_name['tally_params']._options = None
  _GENESISSTATE.fields_by_name['tally_params']._serialized_options = b'\310\336\037\000\362\336\037\023yaml:\"tally_params\"'
  _GENESISSTATE._serialized_start=109
  _GENESISSTATE._serialized_end=636
# @@protoc_insertion_point(module_scope)
