import multiprocessing
import shutil
import time
from os import path

import pytest
import requests

from tests.conftest import get_test_messages
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
from thoughts.server import server

_SERVER_HOST = '127.0.0.1'
_SERVER_PORT = '8003'
_DATA_DIR = './data'


@pytest.fixture(scope="module")
def init_server():
    process = multiprocessing.Process(target=server.run_server, args=(_SERVER_HOST, _SERVER_PORT, None, _DATA_DIR))
    process.start()
    print('Waiting for server to start...')
    time.sleep(5)

    yield process

    process.terminate()
    process.join()
    if path.exists(_DATA_DIR):
        shutil.rmtree(_DATA_DIR)


def test_server(init_server):
    # try:
    encoder = ProtoBufSerializer()
    address = f'http://{_SERVER_HOST}:{_SERVER_PORT}/snapshot'
    for (user, snapshot) in get_test_messages():
        r = requests.post(url=address, data=encoder.message_encode(user, snapshot))
        assert r.status_code == 200


def test_server_bad_request(init_server):
    address = f'http://{_SERVER_HOST}:{_SERVER_PORT}/snapshot'
    r = requests.post(url=address, data='ERR')
    assert r.status_code == 400
    encoder = ProtoBufSerializer()
    for (user, snapshot) in get_test_messages(1):
        encoded_message = encoder.message_encode(user, snapshot)
        encoded_message = encoded_message[0:len(encoded_message) - 1]
        r = requests.post(url=address, data=encoded_message)
        assert r.status_code == 400
