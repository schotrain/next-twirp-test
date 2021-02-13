# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='nextTwirpTest.user',
  syntax='proto3',
  serialized_options=b'Z\004user',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nuser.proto\x12\x12nextTwirpTest.user\"^\n\x08UserInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x11\n\tgivenName\x18\x03 \x01(\t\x12\x12\n\nfamilyName\x18\x04 \x01(\t\x12\x10\n\x08imageUrl\x18\x05 \x01(\t\"\x81\x01\n\x15GetAccessTokenRequest\x12>\n\x10identityProvider\x18\x01 \x01(\x0e\x32$.nextTwirpTest.user.IdentityProvider\x12\x1a\n\x12identityProviderId\x18\x02 \x01(\t\x12\x0c\n\x04hmac\x18\x03 \x01(\t\"-\n\x16GetAccessTokenResponse\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x01 \x01(\t\"\x14\n\x12GetUserInfoRequest\"E\n\x13GetUserInfoResponse\x12.\n\x08userInfo\x18\x01 \x01(\x0b\x32\x1c.nextTwirpTest.user.UserInfo\"K\n\x13SaveUserInfoRequest\x12\x11\n\tgivenName\x18\x01 \x01(\t\x12\x12\n\nfamilyName\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"F\n\x14SaveUserInfoResponse\x12.\n\x08userInfo\x18\x01 \x01(\x0b\x32\x1c.nextTwirpTest.user.UserInfo*(\n\x10IdentityProvider\x12\n\n\x06GOOGLE\x10\x00\x12\x08\n\x04OKTA\x10\x01\x32\xb2\x02\n\x04User\x12g\n\x0egetAccessToken\x12).nextTwirpTest.user.GetAccessTokenRequest\x1a*.nextTwirpTest.user.GetAccessTokenResponse\x12^\n\x0bgetUserInfo\x12&.nextTwirpTest.user.GetUserInfoRequest\x1a\'.nextTwirpTest.user.GetUserInfoResponse\x12\x61\n\x0csaveUserInfo\x12\'.nextTwirpTest.user.SaveUserInfoRequest\x1a(.nextTwirpTest.user.SaveUserInfoResponseB\x06Z\x04userb\x06proto3'
)

_IDENTITYPROVIDER = _descriptor.EnumDescriptor(
  name='IdentityProvider',
  full_name='nextTwirpTest.user.IdentityProvider',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OKTA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=551,
  serialized_end=591,
)
_sym_db.RegisterEnumDescriptor(_IDENTITYPROVIDER)

IdentityProvider = enum_type_wrapper.EnumTypeWrapper(_IDENTITYPROVIDER)
GOOGLE = 0
OKTA = 1



_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='nextTwirpTest.user.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='nextTwirpTest.user.UserInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='nextTwirpTest.user.UserInfo.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='givenName', full_name='nextTwirpTest.user.UserInfo.givenName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='familyName', full_name='nextTwirpTest.user.UserInfo.familyName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imageUrl', full_name='nextTwirpTest.user.UserInfo.imageUrl', index=4,
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
  serialized_start=34,
  serialized_end=128,
)


_GETACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='GetAccessTokenRequest',
  full_name='nextTwirpTest.user.GetAccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identityProvider', full_name='nextTwirpTest.user.GetAccessTokenRequest.identityProvider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identityProviderId', full_name='nextTwirpTest.user.GetAccessTokenRequest.identityProviderId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hmac', full_name='nextTwirpTest.user.GetAccessTokenRequest.hmac', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=131,
  serialized_end=260,
)


_GETACCESSTOKENRESPONSE = _descriptor.Descriptor(
  name='GetAccessTokenResponse',
  full_name='nextTwirpTest.user.GetAccessTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessToken', full_name='nextTwirpTest.user.GetAccessTokenResponse.accessToken', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=262,
  serialized_end=307,
)


_GETUSERINFOREQUEST = _descriptor.Descriptor(
  name='GetUserInfoRequest',
  full_name='nextTwirpTest.user.GetUserInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=309,
  serialized_end=329,
)


_GETUSERINFORESPONSE = _descriptor.Descriptor(
  name='GetUserInfoResponse',
  full_name='nextTwirpTest.user.GetUserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='nextTwirpTest.user.GetUserInfoResponse.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=331,
  serialized_end=400,
)


_SAVEUSERINFOREQUEST = _descriptor.Descriptor(
  name='SaveUserInfoRequest',
  full_name='nextTwirpTest.user.SaveUserInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='givenName', full_name='nextTwirpTest.user.SaveUserInfoRequest.givenName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='familyName', full_name='nextTwirpTest.user.SaveUserInfoRequest.familyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='nextTwirpTest.user.SaveUserInfoRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=402,
  serialized_end=477,
)


_SAVEUSERINFORESPONSE = _descriptor.Descriptor(
  name='SaveUserInfoResponse',
  full_name='nextTwirpTest.user.SaveUserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='nextTwirpTest.user.SaveUserInfoResponse.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=479,
  serialized_end=549,
)

_GETACCESSTOKENREQUEST.fields_by_name['identityProvider'].enum_type = _IDENTITYPROVIDER
_GETUSERINFORESPONSE.fields_by_name['userInfo'].message_type = _USERINFO
_SAVEUSERINFORESPONSE.fields_by_name['userInfo'].message_type = _USERINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['GetAccessTokenRequest'] = _GETACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetAccessTokenResponse'] = _GETACCESSTOKENRESPONSE
DESCRIPTOR.message_types_by_name['GetUserInfoRequest'] = _GETUSERINFOREQUEST
DESCRIPTOR.message_types_by_name['GetUserInfoResponse'] = _GETUSERINFORESPONSE
DESCRIPTOR.message_types_by_name['SaveUserInfoRequest'] = _SAVEUSERINFOREQUEST
DESCRIPTOR.message_types_by_name['SaveUserInfoResponse'] = _SAVEUSERINFORESPONSE
DESCRIPTOR.enum_types_by_name['IdentityProvider'] = _IDENTITYPROVIDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

GetAccessTokenRequest = _reflection.GeneratedProtocolMessageType('GetAccessTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCESSTOKENREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.GetAccessTokenRequest)
  })
_sym_db.RegisterMessage(GetAccessTokenRequest)

GetAccessTokenResponse = _reflection.GeneratedProtocolMessageType('GetAccessTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCESSTOKENRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.GetAccessTokenResponse)
  })
_sym_db.RegisterMessage(GetAccessTokenResponse)

GetUserInfoRequest = _reflection.GeneratedProtocolMessageType('GetUserInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERINFOREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.GetUserInfoRequest)
  })
_sym_db.RegisterMessage(GetUserInfoRequest)

GetUserInfoResponse = _reflection.GeneratedProtocolMessageType('GetUserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERINFORESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.GetUserInfoResponse)
  })
_sym_db.RegisterMessage(GetUserInfoResponse)

SaveUserInfoRequest = _reflection.GeneratedProtocolMessageType('SaveUserInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVEUSERINFOREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.SaveUserInfoRequest)
  })
_sym_db.RegisterMessage(SaveUserInfoRequest)

SaveUserInfoResponse = _reflection.GeneratedProtocolMessageType('SaveUserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVEUSERINFORESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:nextTwirpTest.user.SaveUserInfoResponse)
  })
_sym_db.RegisterMessage(SaveUserInfoResponse)


DESCRIPTOR._options = None

_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='nextTwirpTest.user.User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=594,
  serialized_end=900,
  methods=[
  _descriptor.MethodDescriptor(
    name='getAccessToken',
    full_name='nextTwirpTest.user.User.getAccessToken',
    index=0,
    containing_service=None,
    input_type=_GETACCESSTOKENREQUEST,
    output_type=_GETACCESSTOKENRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getUserInfo',
    full_name='nextTwirpTest.user.User.getUserInfo',
    index=1,
    containing_service=None,
    input_type=_GETUSERINFOREQUEST,
    output_type=_GETUSERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='saveUserInfo',
    full_name='nextTwirpTest.user.User.saveUserInfo',
    index=2,
    containing_service=None,
    input_type=_SAVEUSERINFOREQUEST,
    output_type=_SAVEUSERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
