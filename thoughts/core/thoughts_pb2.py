# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thoughts.proto

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
  name='thoughts.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0ethoughts.proto\"\x84\x01\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08\x62irthday\x18\x03 \x01(\r\x12\x1c\n\x06gender\x18\x04 \x01(\x0e\x32\x0c.User.Gender\")\n\x06Gender\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\t\n\x05OTHER\x10\x02\"\xb8\x01\n\x08Snapshot\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\x04\x12\x13\n\x04pose\x18\x04 \x01(\x0b\x32\x05.Pose\x12 \n\x0b\x63olor_image\x18\x05 \x01(\x0b\x32\x0b.ColorImage\x12 \n\x0b\x64\x65pth_image\x18\x06 \x01(\x0b\x32\x0b.DepthImage\x12\x1b\n\x08\x66\x65\x65lings\x18\x07 \x01(\x0b\x32\t.Feelings\"\xaa\x01\n\x10\x45nrichedSnapshot\x12\x10\n\x08\x64\x61tetime\x18\x01 \x01(\x04\x12\x13\n\x04pose\x18\x02 \x01(\x0b\x32\x05.Pose\x12(\n\x0b\x63olor_image\x18\x03 \x01(\x0b\x32\x13.EnrichedColorImage\x12(\n\x0b\x64\x65pth_image\x18\x04 \x01(\x0b\x32\x13.EnrichedDepthImage\x12\x1b\n\x08\x66\x65\x65lings\x18\x05 \x01(\x0b\x32\t.Feelings\"\xb8\x01\n\x04Pose\x12&\n\x0btranslation\x18\x01 \x01(\x0b\x32\x11.Pose.Translation\x12 \n\x08rotation\x18\x02 \x01(\x0b\x32\x0e.Pose.Rotation\x1a.\n\x0bTranslation\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x1a\x36\n\x08Rotation\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\"9\n\nColorImage\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0c\n\x04path\x18\x03 \x01(\t\"9\n\nDepthImage\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0c\n\x04path\x18\x03 \x01(\t\"A\n\x12\x45nrichedColorImage\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"A\n\x12\x45nrichedDepthImage\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x02\"Q\n\x08\x46\x65\x65lings\x12\x0e\n\x06hunger\x18\x01 \x01(\x02\x12\x0e\n\x06thirst\x18\x02 \x01(\x02\x12\x12\n\nexhaustion\x18\x03 \x01(\x02\x12\x11\n\thappiness\x18\x04 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USER_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='User.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MALE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=110,
  serialized_end=151,
)
_sym_db.RegisterEnumDescriptor(_USER_GENDER)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='User.user_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='birthday', full_name='User.birthday', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='User.gender', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_GENDER,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=151,
)


_SNAPSHOT = _descriptor.Descriptor(
  name='Snapshot',
  full_name='Snapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='Snapshot.snapshot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Snapshot.user_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='Snapshot.datetime', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose', full_name='Snapshot.pose', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color_image', full_name='Snapshot.color_image', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth_image', full_name='Snapshot.depth_image', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feelings', full_name='Snapshot.feelings', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=154,
  serialized_end=338,
)


_ENRICHEDSNAPSHOT = _descriptor.Descriptor(
  name='EnrichedSnapshot',
  full_name='EnrichedSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datetime', full_name='EnrichedSnapshot.datetime', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pose', full_name='EnrichedSnapshot.pose', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color_image', full_name='EnrichedSnapshot.color_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='depth_image', full_name='EnrichedSnapshot.depth_image', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feelings', full_name='EnrichedSnapshot.feelings', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=341,
  serialized_end=511,
)


_POSE_TRANSLATION = _descriptor.Descriptor(
  name='Translation',
  full_name='Pose.Translation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Pose.Translation.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Pose.Translation.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='Pose.Translation.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=596,
  serialized_end=642,
)

_POSE_ROTATION = _descriptor.Descriptor(
  name='Rotation',
  full_name='Pose.Rotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Pose.Rotation.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Pose.Rotation.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='Pose.Rotation.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='Pose.Rotation.w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=644,
  serialized_end=698,
)

_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='Pose.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='Pose.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_POSE_TRANSLATION, _POSE_ROTATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=698,
)


_COLORIMAGE = _descriptor.Descriptor(
  name='ColorImage',
  full_name='ColorImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='ColorImage.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='ColorImage.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='ColorImage.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=757,
)


_DEPTHIMAGE = _descriptor.Descriptor(
  name='DepthImage',
  full_name='DepthImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='DepthImage.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='DepthImage.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='DepthImage.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=816,
)


_ENRICHEDCOLORIMAGE = _descriptor.Descriptor(
  name='EnrichedColorImage',
  full_name='EnrichedColorImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='EnrichedColorImage.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='EnrichedColorImage.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='EnrichedColorImage.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=818,
  serialized_end=883,
)


_ENRICHEDDEPTHIMAGE = _descriptor.Descriptor(
  name='EnrichedDepthImage',
  full_name='EnrichedDepthImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='EnrichedDepthImage.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='EnrichedDepthImage.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='EnrichedDepthImage.data', index=2,
      number=3, type=2, cpp_type=6, label=3,
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
  serialized_start=885,
  serialized_end=950,
)


_FEELINGS = _descriptor.Descriptor(
  name='Feelings',
  full_name='Feelings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hunger', full_name='Feelings.hunger', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thirst', full_name='Feelings.thirst', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exhaustion', full_name='Feelings.exhaustion', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='happiness', full_name='Feelings.happiness', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=952,
  serialized_end=1033,
)

_USER.fields_by_name['gender'].enum_type = _USER_GENDER
_USER_GENDER.containing_type = _USER
_SNAPSHOT.fields_by_name['pose'].message_type = _POSE
_SNAPSHOT.fields_by_name['color_image'].message_type = _COLORIMAGE
_SNAPSHOT.fields_by_name['depth_image'].message_type = _DEPTHIMAGE
_SNAPSHOT.fields_by_name['feelings'].message_type = _FEELINGS
_ENRICHEDSNAPSHOT.fields_by_name['pose'].message_type = _POSE
_ENRICHEDSNAPSHOT.fields_by_name['color_image'].message_type = _ENRICHEDCOLORIMAGE
_ENRICHEDSNAPSHOT.fields_by_name['depth_image'].message_type = _ENRICHEDDEPTHIMAGE
_ENRICHEDSNAPSHOT.fields_by_name['feelings'].message_type = _FEELINGS
_POSE_TRANSLATION.containing_type = _POSE
_POSE_ROTATION.containing_type = _POSE
_POSE.fields_by_name['translation'].message_type = _POSE_TRANSLATION
_POSE.fields_by_name['rotation'].message_type = _POSE_ROTATION
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Snapshot'] = _SNAPSHOT
DESCRIPTOR.message_types_by_name['EnrichedSnapshot'] = _ENRICHEDSNAPSHOT
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['ColorImage'] = _COLORIMAGE
DESCRIPTOR.message_types_by_name['DepthImage'] = _DEPTHIMAGE
DESCRIPTOR.message_types_by_name['EnrichedColorImage'] = _ENRICHEDCOLORIMAGE
DESCRIPTOR.message_types_by_name['EnrichedDepthImage'] = _ENRICHEDDEPTHIMAGE
DESCRIPTOR.message_types_by_name['Feelings'] = _FEELINGS

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)

Snapshot = _reflection.GeneratedProtocolMessageType('Snapshot', (_message.Message,), dict(
  DESCRIPTOR = _SNAPSHOT,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:Snapshot)
  ))
_sym_db.RegisterMessage(Snapshot)

EnrichedSnapshot = _reflection.GeneratedProtocolMessageType('EnrichedSnapshot', (_message.Message,), dict(
  DESCRIPTOR = _ENRICHEDSNAPSHOT,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:EnrichedSnapshot)
  ))
_sym_db.RegisterMessage(EnrichedSnapshot)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(

  Translation = _reflection.GeneratedProtocolMessageType('Translation', (_message.Message,), dict(
    DESCRIPTOR = _POSE_TRANSLATION,
    __module__ = 'thoughts_pb2'
    # @@protoc_insertion_point(class_scope:Pose.Translation)
    ))
  ,

  Rotation = _reflection.GeneratedProtocolMessageType('Rotation', (_message.Message,), dict(
    DESCRIPTOR = _POSE_ROTATION,
    __module__ = 'thoughts_pb2'
    # @@protoc_insertion_point(class_scope:Pose.Rotation)
    ))
  ,
  DESCRIPTOR = _POSE,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:Pose)
  ))
_sym_db.RegisterMessage(Pose)
_sym_db.RegisterMessage(Pose.Translation)
_sym_db.RegisterMessage(Pose.Rotation)

ColorImage = _reflection.GeneratedProtocolMessageType('ColorImage', (_message.Message,), dict(
  DESCRIPTOR = _COLORIMAGE,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:ColorImage)
  ))
_sym_db.RegisterMessage(ColorImage)

DepthImage = _reflection.GeneratedProtocolMessageType('DepthImage', (_message.Message,), dict(
  DESCRIPTOR = _DEPTHIMAGE,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:DepthImage)
  ))
_sym_db.RegisterMessage(DepthImage)

EnrichedColorImage = _reflection.GeneratedProtocolMessageType('EnrichedColorImage', (_message.Message,), dict(
  DESCRIPTOR = _ENRICHEDCOLORIMAGE,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:EnrichedColorImage)
  ))
_sym_db.RegisterMessage(EnrichedColorImage)

EnrichedDepthImage = _reflection.GeneratedProtocolMessageType('EnrichedDepthImage', (_message.Message,), dict(
  DESCRIPTOR = _ENRICHEDDEPTHIMAGE,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:EnrichedDepthImage)
  ))
_sym_db.RegisterMessage(EnrichedDepthImage)

Feelings = _reflection.GeneratedProtocolMessageType('Feelings', (_message.Message,), dict(
  DESCRIPTOR = _FEELINGS,
  __module__ = 'thoughts_pb2'
  # @@protoc_insertion_point(class_scope:Feelings)
  ))
_sym_db.RegisterMessage(Feelings)


# @@protoc_insertion_point(module_scope)
