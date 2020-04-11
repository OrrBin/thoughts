import requests
from thoughts.utils.file_reader import FileReader
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

encoder = ProtoBufSerializer()


def upload_sample(host, port, path="sample.mind.gz"):
    """
    Reads all snapshots from the given sample, and sends them to the server
    :param host: server host
    :param port: server port
    :param path: path to the sample file
    """
    reader = FileReader(path)

    user = reader.get_user()
    success_count = 0
    fail_count = 0
    i = 0
    try:
        for snapshot in reader:
            i += 1
            # snapshot = reader.get_enriched_snapshot()
            address = f'http://{host}:{port}/snapshot'
            r = requests.post(url=address, data=encoder.message_encode(user, snapshot))
            if r.status_code != 200:
                print(f'snapshot number {i} failed to send')
                fail_count += 1
            else:
                success_count += 1
    except KeyboardInterrupt:
        print(f'Got termination signal')
    except Exception as e:
        print(f'Error encountered')
        raise e

    print(f'{success_count} snapshots was sent successfully, {fail_count} failed to send')
