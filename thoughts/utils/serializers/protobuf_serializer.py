import struct
import io

from google.protobuf.message import DecodeError

from thoughts.core.thoughts_pb2 import User
from thoughts.core.thoughts_pb2 import Snapshot, EnrichedSnapshot


class ProtoBufSerializer:
    def user_encode(self, user):
        return user.SerializeToString()

    def user_decode(self, user_bytes):
        user = User()
        try:
            user.ParseFromString(user_bytes)
        except DecodeError as e:
            raise DecodeError(f'Encountered error while decoding user: {e}')
        return user

    def snapshot_encode(self, snapshot):
        return snapshot.SerializeToString()

    def snapshot_decode(self, snapshot_bytes):
        snapshot = Snapshot()
        try:
            snapshot.ParseFromString(snapshot_bytes)
        except DecodeError as e:
            raise DecodeError(f'Encountered error while decoding snapshot: {e}')
        return snapshot

    def enriched_snapshot_encode(self, snapshot):
        return snapshot.SerializeToString()

    def enriched_snapshot_decode(self, snapshot_bytes):
        snapshot = EnrichedSnapshot()
        snapshot.ParseFromString(snapshot_bytes)
        return snapshot

    def message_encode(self, user, snapshot):
        user_bytes = self.user_encode(user)
        snapshot_bytes = self.enriched_snapshot_encode(snapshot)
        user_len = struct.pack('I', len(user_bytes))
        snapshot_len = struct.pack('I', len(snapshot_bytes))
        return user_len + user_bytes + snapshot_len + snapshot_bytes

    def message_decode(self, message_bytes):
        stream = io.BytesIO(message_bytes)
        try:
            user_len, = struct.unpack('I', stream.read(4))
            user_bytes = stream.read(user_len)
        except struct.error:
            raise ValueError('Bad message format, could not unpack user')

        try:
            snapshot_len, = struct.unpack('I', stream.read(4))
            snapshot_bytes = stream.read(snapshot_len)
        except struct.error:
            raise ValueError('Bad message format, could not unpack snapshot')

        try:
            user = self.user_decode(user_bytes)
        except DecodeError:
            raise ValueError('Bad message format, could not decode user')
        try:
            snapshot = self.enriched_snapshot_decode(snapshot_bytes)
        except DecodeError:
            raise ValueError('Bad message format, could not decode snapshot')

        return [user, snapshot]
