from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
from tests.conftest import get_test_snapshots, get_test_users


def test_protobuf_serializer():
    serializer = ProtoBufSerializer()
    for snapshot in get_test_snapshots():
        snap_str = serializer.snapshot_encode(snapshot)
        new_snap = serializer.snapshot_decode(snap_str)
        assert new_snap == snapshot

    for user in get_test_users():
        user_str = serializer.user_encode(user)
        new_user = serializer.user_decode(user_str)
        assert new_user == user


