# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: score_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'score_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13score_service.proto\x12\x05score\" \n\x0fGetScoreRequest\x12\r\n\x05login\x18\x01 \x01(\t\"\x1e\n\rScoreResponse\x12\r\n\x05score\x18\x01 \x01(\x02\"$\n\x14GenerateScoreRequest\x12\x0c\n\x04good\x18\x01 \x01(\x08\"5\n\x16RegenerateScoreRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x0c\n\x04good\x18\x02 \x01(\x08\"%\n\x14\x45valuateScoreRequest\x12\r\n\x05login\x18\x01 \x01(\t\"&\n\x15\x45valuateScoreResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x32\xa0\x02\n\x0cScoreService\x12\x38\n\x08GetScore\x12\x16.score.GetScoreRequest\x1a\x14.score.ScoreResponse\x12\x46\n\x0fRegenerateScore\x12\x1d.score.RegenerateScoreRequest\x1a\x14.score.ScoreResponse\x12J\n\rEvaluateScore\x12\x1b.score.EvaluateScoreRequest\x1a\x1c.score.EvaluateScoreResponse\x12\x42\n\rGenerateScore\x12\x1b.score.GenerateScoreRequest\x1a\x14.score.ScoreResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'score_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETSCOREREQUEST']._serialized_start=30
  _globals['_GETSCOREREQUEST']._serialized_end=62
  _globals['_SCORERESPONSE']._serialized_start=64
  _globals['_SCORERESPONSE']._serialized_end=94
  _globals['_GENERATESCOREREQUEST']._serialized_start=96
  _globals['_GENERATESCOREREQUEST']._serialized_end=132
  _globals['_REGENERATESCOREREQUEST']._serialized_start=134
  _globals['_REGENERATESCOREREQUEST']._serialized_end=187
  _globals['_EVALUATESCOREREQUEST']._serialized_start=189
  _globals['_EVALUATESCOREREQUEST']._serialized_end=226
  _globals['_EVALUATESCORERESPONSE']._serialized_start=228
  _globals['_EVALUATESCORERESPONSE']._serialized_end=266
  _globals['_SCORESERVICE']._serialized_start=269
  _globals['_SCORESERVICE']._serialized_end=557
# @@protoc_insertion_point(module_scope)