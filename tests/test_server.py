import multiprocessing
import shutil
import time
from os import path

import requests

from tests.conftest import get_test_messages
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
from thoughts.server import server

_SERVER_HOST = '127.0.0.1'
_SERVER_PORT = '8003'
_DATA_DIR = './data'


def test_server():
    process = multiprocessing.Process(target=server.run_server, args=(_SERVER_HOST, _SERVER_PORT, None, _DATA_DIR))
    process.start()

    print('Waiting for server to start...')
    time.sleep(5)

    try:
        encoder = ProtoBufSerializer()
        address = f'http://{_SERVER_HOST}:{_SERVER_PORT}/snapshot'
        for (user, snapshot) in get_test_messages():
            r = requests.post(url=address, data=encoder.message_encode(user, snapshot))
            assert r.status_code == 200

    finally:
        process.terminate()
        process.join()
        if path.exists(_DATA_DIR):
            shutil.rmtree(_DATA_DIR)
