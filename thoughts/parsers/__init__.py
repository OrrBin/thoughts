import importlib
import json
import sys
from pathlib import Path
from threading import Thread

from google.protobuf.message import DecodeError

from thoughts.message_queues import init_queue
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

from thoughts.server import  server

_DATA_DIR = server.root_data_dir()

config = {}
pbs = ProtoBufSerializer()


def load_parsers():
    """
    Collects parsers and registers them.
    Registers all functions that ends with 'parse' according to their identifier attribute.
    For example for parser with identifier attribute equals to color_image
    It would be registered under color_image.

    To add a new parser add a function, implement the parser and add identifier attribute
    with the specific parser type.
    The parser function must get one parameter, the snapshots bytes.

    And must return dict with one element: {identifier: value}
    Where value is the parsed value, and identifier is the parser identifier
    """
    root = Path("thoughts/parsers").absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or not file.suffix == '.py':
            continue
        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)
        for key, func in module.__dict__.items():
            if callable(func) and func.__name__.startswith("parse"):
                config[func.identifier] = func


def parse(parser_name, raw_data, data_dir):
    return config[parser_name](raw_data, data_dir)


def run_parser(parser_name, mq_url, data_dir=_DATA_DIR):
    """
    Registering parser of the given name to listen to the message queue to incoming snapshots.
    On each incoming snapshot, running the parser, enriching it's result and publishing to message queue
    :param parser_name: parser name to run
    :param mq_url: message queue to pubkish to
    :param data_dir: root directory for all data and images
    """
    mq = init_queue(mq_url)

    def handler(body):
        try:
            result = parse(parser_name, body, data_dir)
        except Exception:
            print(f'Parser {parser_name} failed to parse message')
            return

        try:
            snapshot = pbs.snapshot_decode(body)
        except DecodeError as e:
            print(e)
            return

        result = dict(
            snapshot_id=snapshot.snapshot_id,
            user_id=snapshot.user_id,
            timestamp=snapshot.datetime,
            data=result
        )

        result = json.dumps(result)

        print(f"Parsed {parser_name}")
        mq.publish(parser_name, result)

    mq.consume('snapshot', handler)


def run_all_parsers(mq_url, data_dir=_DATA_DIR):
    for parser_name in get_available_parsers():
        t = Thread(target=run_parser, args=(parser_name, mq_url, data_dir))
        t.start()
        print(f'Parser {parser_name} is activated')


def run_one_parser(parser_name, mq_url, data_dir=_DATA_DIR):
    t = Thread(target=run_parser, args=(parser_name, mq_url, data_dir))
    t.start()
    print(f'Parser {parser_name} is activated')


def get_available_parsers():
    return list(config.keys())


load_parsers()
