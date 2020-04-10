import requests
from thoughts.utils.file_reader import FileReader
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

encoder = ProtoBufSerializer()


def upload_sample(host, port, path="sample.mind.gz"):
    reader = FileReader(path)

    user = reader.get_user()
    for i in range (1,2):
        snapshot = reader.get_enriched_snapshot()
        address = f'http://{host}:{port}/snapshot'
        r = requests.post(url=address, data=encoder.message_encode(user, snapshot))
        if r.status_code != 200:
            print(f'snapshot {i} failed to send')

    print(f'Snapshots was sent unsuccessfully')