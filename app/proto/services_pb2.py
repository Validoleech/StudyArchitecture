# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services.proto
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
    'services.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\x12\x03\x61pp\"\x1d\n\x0cLoginRequest\x12\r\n\x05login\x18\x01 \x01(\t\"0\n\x11ResetScoreRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x0c\n\x04good\x18\x02 \x01(\x08\".\n\x0b\x41uthRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\">\n\x0cUserResponse\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\"3\n\x0c\x41uthResponse\x12\x12\n\nauthorized\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"M\n\rScoreResponse\x12\r\n\x05login\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x02\x12\r\n\x05valid\x18\x04 \x01(\x08\"3\n\x10PasswordResponse\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t2\xab\x01\n\x0cScoreService\x12\x31\n\x08GetScore\x12\x11.app.LoginRequest\x1a\x12.app.ScoreResponse\x12\x37\n\x0bGetPassword\x12\x11.app.LoginRequest\x1a\x15.app.PasswordResponse\x12/\n\x06GetGud\x12\x11.app.LoginRequest\x1a\x12.app.ScoreResponse2?\n\x0b\x41uthService\x12\x30\n\tAuthorize\x12\x10.app.AuthRequest\x1a\x11.app.AuthResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGINREQUEST']._serialized_start=23
  _globals['_LOGINREQUEST']._serialized_end=52
  _globals['_RESETSCOREREQUEST']._serialized_start=54
  _globals['_RESETSCOREREQUEST']._serialized_end=102
  _globals['_AUTHREQUEST']._serialized_start=104
  _globals['_AUTHREQUEST']._serialized_end=150
  _globals['_USERRESPONSE']._serialized_start=152
  _globals['_USERRESPONSE']._serialized_end=214
  _globals['_AUTHRESPONSE']._serialized_start=216
  _globals['_AUTHRESPONSE']._serialized_end=267
  _globals['_SCORERESPONSE']._serialized_start=269
  _globals['_SCORERESPONSE']._serialized_end=346
  _globals['_PASSWORDRESPONSE']._serialized_start=348
  _globals['_PASSWORDRESPONSE']._serialized_end=399
  _globals['_SCORESERVICE']._serialized_start=402
  _globals['_SCORESERVICE']._serialized_end=573
  _globals['_AUTHSERVICE']._serialized_start=575
  _globals['_AUTHSERVICE']._serialized_end=638
# @@protoc_insertion_point(module_scope)