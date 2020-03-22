import json

from thoughts.serializers.protobuf_serializer import ProtoBufSerializer

pbs = ProtoBufSerializer()


def parse_pose(snapshot_bytes):
    snapshot = pbs.snapshot_decode(snapshot_bytes)
    rotation = dict(
        x=snapshot.pose.rotation.x,
        y=snapshot.pose.rotation.y,
        z=snapshot.pose.rotation.z,
        w=snapshot.pose.rotation.w)

    translation = dict(
        x=snapshot.pose.translation.x,
        y=snapshot.pose.translation.y,
        z=snapshot.pose.translation.z)

    pose = dict(
        translation=translation,
        rotation=rotation)

    pose = dict(pose=pose)

    return pose


parse_pose.field = 'pose'
