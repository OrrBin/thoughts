import importlib
import json
import sys
from pathlib import Path
from threading import Thread

from thoughts.message_queues import init_queue
from thoughts.serializers.protobuf_serializer import ProtoBufSerializer

config = {}
pbs = ProtoBufSerializer()


def load_parsers():
    root = Path("thoughts/parsers").absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or not file.suffix == '.py':
            continue
        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)
        for key, func in module.__dict__.items():
            if callable(func) and func.__name__.startswith("parse"):
                config[func.identifier] = func


def parse(parser_name, raw_data):
    return config[parser_name](raw_data)


def run_parser(parser_name, mq_url):
    mq = init_queue(mq_url)

    def handler(body):
        result = parse(parser_name, body)

        snapshot = pbs.snapshot_decode(body)
        result = dict(
            snapshot_id=snapshot.snapshot_id,
            data=result
        )

        result = json.dumps(result)

        print(f"Parsed {parser_name}")
        mq.publish(parser_name, result)

    mq.consume('snapshot', handler)


def run_all_parsers(mq_url):
    for parser_name in get_available_parsers():
        t = Thread(target=run_parser, args=(parser_name, mq_url))
        t.start()
        print(f'Parser {parser_name} is activated')


def get_available_parsers():
    return list(config.keys())


load_parsers()
