from .protobuf_file_reader import ProtobufFileReader

DEFAULT_FILE_READER = ProtobufFileReader


class FileReader:
    def __init__(self, path, format_reader=None):
        self.path = path
        if not format_reader:
            format_reader = DEFAULT_FILE_READER()
        self.format_reader = format_reader

        self.format_reader.open_file(path)
        self.user = self.format_reader.get_user_information()

    def get_user(self):
        return self.user

    def get_snapshot(self):
        return self.format_reader.get_snapshot()

    def get_enriched_snapshot(self):
        return self.format_reader.get_enriched_snapshot()

    def __repr__(self):
        path = self.path
        return f'Reader({path=}, user={self.user.username})'

    def __str__(self):
        path = self.path
        return f'Reader({path=}, user={self.user.username})'

    def __iter__(self):
        snapshot = self.format_reader.get_snapshot()
        while snapshot:
            yield snapshot
            snapshot = self.format_reader.get_enriched_snapshot()

    def close(self):
        self.format_reader.stream.close()
