# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/types/validator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tendermint/types/validator.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/crypto/keys.proto\"\xb2\x01\n\x0cValidatorSet\x12;\n\nvalidators\x18\x01 \x03(\x0b\x32\x1b.tendermint.types.ValidatorR\nvalidators\x12\x37\n\x08proposer\x18\x02 \x01(\x0b\x32\x1b.tendermint.types.ValidatorR\x08proposer\x12,\n\x12total_voting_power\x18\x03 \x01(\x03R\x10totalVotingPower\"\xb2\x01\n\tValidator\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0cR\x07\x61\x64\x64ress\x12;\n\x07pub_key\x18\x02 \x01(\x0b\x32\x1c.tendermint.crypto.PublicKeyB\x04\xc8\xde\x1f\x00R\x06pubKey\x12!\n\x0cvoting_power\x18\x03 \x01(\x03R\x0bvotingPower\x12+\n\x11proposer_priority\x18\x04 \x01(\x03R\x10proposerPriority\"k\n\x0fSimpleValidator\x12\x35\n\x07pub_key\x18\x01 \x01(\x0b\x32\x1c.tendermint.crypto.PublicKeyR\x06pubKey\x12!\n\x0cvoting_power\x18\x02 \x01(\x03R\x0bvotingPowerB5Z3github.com/cometbft/cometbft/proto/tendermint/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.validator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/cometbft/cometbft/proto/tendermint/types'
  _VALIDATOR.fields_by_name['pub_key']._options = None
  _VALIDATOR.fields_by_name['pub_key']._serialized_options = b'\310\336\037\000'
  _VALIDATORSET._serialized_start=107
  _VALIDATORSET._serialized_end=285
  _VALIDATOR._serialized_start=288
  _VALIDATOR._serialized_end=466
  _SIMPLEVALIDATOR._serialized_start=468
  _SIMPLEVALIDATOR._serialized_end=575
# @@protoc_insertion_point(module_scope)