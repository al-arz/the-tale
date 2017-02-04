# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='diary.proto',
  package='diary',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x64iary.proto\x12\x05\x64iary\"\xec\x01\n\x07Message\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x13\n\x0bturn_number\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x03 \x01(\r\x12\x11\n\tgame_time\x18\x04 \x01(\t\x12\x11\n\tgame_date\x18\x05 \x01(\t\x12\x10\n\x08position\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x30\n\tvariables\x18\x08 \x03(\x0b\x32\x1d.diary.Message.VariablesEntry\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x05\x44iary\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12 \n\x08messages\x18\x02 \x03(\x0b\x32\x0e.diary.Message\"$\n\x0eVersionRequest\x12\x12\n\naccount_id\x18\x01 \x01(\r\"\"\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\x04\"]\n\x12PushMessageRequest\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x12\n\ndiary_size\x18\x02 \x01(\r\x12\x1f\n\x07message\x18\x03 \x01(\x0b\x32\x0e.diary.Message\"\x15\n\x13PushMessageResponse\"\"\n\x0c\x44iaryRequest\x12\x12\n\naccount_id\x18\x01 \x01(\r\",\n\rDiaryResponse\x12\x1b\n\x05\x64iary\x18\x01 \x01(\x0b\x32\x0c.diary.Diaryb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MESSAGE_VARIABLESENTRY = _descriptor.Descriptor(
  name='VariablesEntry',
  full_name='diary.Message.VariablesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='diary.Message.VariablesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='diary.Message.VariablesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=259,
)

_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='diary.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='diary.Message.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turn_number', full_name='diary.Message.turn_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='diary.Message.type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_time', full_name='diary.Message.game_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_date', full_name='diary.Message.game_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='diary.Message.position', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='diary.Message.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variables', full_name='diary.Message.variables', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_VARIABLESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=259,
)


_DIARY = _descriptor.Descriptor(
  name='Diary',
  full_name='diary.Diary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='diary.Diary.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='diary.Diary.messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=319,
)


_VERSIONREQUEST = _descriptor.Descriptor(
  name='VersionRequest',
  full_name='diary.VersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='diary.VersionRequest.account_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=357,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='diary.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='diary.VersionResponse.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=393,
)


_PUSHMESSAGEREQUEST = _descriptor.Descriptor(
  name='PushMessageRequest',
  full_name='diary.PushMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='diary.PushMessageRequest.account_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diary_size', full_name='diary.PushMessageRequest.diary_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='diary.PushMessageRequest.message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=488,
)


_PUSHMESSAGERESPONSE = _descriptor.Descriptor(
  name='PushMessageResponse',
  full_name='diary.PushMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=490,
  serialized_end=511,
)


_DIARYREQUEST = _descriptor.Descriptor(
  name='DiaryRequest',
  full_name='diary.DiaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='diary.DiaryRequest.account_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=547,
)


_DIARYRESPONSE = _descriptor.Descriptor(
  name='DiaryResponse',
  full_name='diary.DiaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diary', full_name='diary.DiaryResponse.diary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=593,
)

_MESSAGE_VARIABLESENTRY.containing_type = _MESSAGE
_MESSAGE.fields_by_name['variables'].message_type = _MESSAGE_VARIABLESENTRY
_DIARY.fields_by_name['messages'].message_type = _MESSAGE
_PUSHMESSAGEREQUEST.fields_by_name['message'].message_type = _MESSAGE
_DIARYRESPONSE.fields_by_name['diary'].message_type = _DIARY
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['Diary'] = _DIARY
DESCRIPTOR.message_types_by_name['VersionRequest'] = _VERSIONREQUEST
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
DESCRIPTOR.message_types_by_name['PushMessageRequest'] = _PUSHMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['PushMessageResponse'] = _PUSHMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['DiaryRequest'] = _DIARYREQUEST
DESCRIPTOR.message_types_by_name['DiaryResponse'] = _DIARYRESPONSE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(

  VariablesEntry = _reflection.GeneratedProtocolMessageType('VariablesEntry', (_message.Message,), dict(
    DESCRIPTOR = _MESSAGE_VARIABLESENTRY,
    __module__ = 'diary_pb2'
    # @@protoc_insertion_point(class_scope:diary.Message.VariablesEntry)
    ))
  ,
  DESCRIPTOR = _MESSAGE,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.Message)
  ))
_sym_db.RegisterMessage(Message)
_sym_db.RegisterMessage(Message.VariablesEntry)

Diary = _reflection.GeneratedProtocolMessageType('Diary', (_message.Message,), dict(
  DESCRIPTOR = _DIARY,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.Diary)
  ))
_sym_db.RegisterMessage(Diary)

VersionRequest = _reflection.GeneratedProtocolMessageType('VersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONREQUEST,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.VersionRequest)
  ))
_sym_db.RegisterMessage(VersionRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONRESPONSE,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.VersionResponse)
  ))
_sym_db.RegisterMessage(VersionResponse)

PushMessageRequest = _reflection.GeneratedProtocolMessageType('PushMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUSHMESSAGEREQUEST,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.PushMessageRequest)
  ))
_sym_db.RegisterMessage(PushMessageRequest)

PushMessageResponse = _reflection.GeneratedProtocolMessageType('PushMessageResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUSHMESSAGERESPONSE,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.PushMessageResponse)
  ))
_sym_db.RegisterMessage(PushMessageResponse)

DiaryRequest = _reflection.GeneratedProtocolMessageType('DiaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _DIARYREQUEST,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.DiaryRequest)
  ))
_sym_db.RegisterMessage(DiaryRequest)

DiaryResponse = _reflection.GeneratedProtocolMessageType('DiaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _DIARYRESPONSE,
  __module__ = 'diary_pb2'
  # @@protoc_insertion_point(class_scope:diary.DiaryResponse)
  ))
_sym_db.RegisterMessage(DiaryResponse)


_MESSAGE_VARIABLESENTRY.has_options = True
_MESSAGE_VARIABLESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
