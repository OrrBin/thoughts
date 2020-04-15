import gzip
import struct
import traceback

from thoughts.core.thoughts_pb2 import User, Snapshot, EnrichedSnapshot

UINT_SIZE = 4


class ProtobufFileReader:
    def __init__(self, path=None):
        self.path = path
        if path:
            self.stream = gzip.open(path, "rb")

    def open_file(self, path):
        self.path = path
        self.stream = gzip.open(path, "rb")

    def _get_data(self):
        data = self.stream.read(UINT_SIZE)
        if not data or len(data) == 0:
            return None

        size, = struct.unpack('I', data)
        return self.stream.read(size)

    def get_user_information(self):
        user_snap = User()
        data = self._get_data()
        if not data:
            return None
        user_snap.ParseFromString(data)
        return user_snap

    def get_snapshot(self):
        proto_snap = Snapshot()
        data = self._get_data()
        if not data:
            return None
        proto_snap.ParseFromString(data)
        return proto_snap

    def get_enriched_snapshot(self):
        proto_snap = EnrichedSnapshot()
        data = self._get_data()
        if not data:
            return None
        proto_snap.ParseFromString(data)
        return proto_snap
