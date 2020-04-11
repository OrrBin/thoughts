import importlib
import sys
from furl import furl
from pathlib import Path

config = {}


def load_message_queues():
    """
    Collects message queue handlers and registers them.
    Registers according to their prefix attribute.
    For example for handler with prefix attribute equals to rabbitmq
    It would be registered under rabbitmq.

    To add a new handler add a file, with name that end with mq.py, implement the handler and add prefix attribute
    with the specific message queue type.
    The handler must implement the functions:
    publish(self, topic, message)
    consume(self, topic, handler)

    And have a constructor accepting: host, port
    """
    root = Path("thoughts/message_queues").absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or not file.suffix == '.py':
            continue
        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)

        for key, mq in module.__dict__.items():
            if isinstance(mq, type) and mq.__name__.endswith("MQ"):
                config[mq.prefix] = mq


def init_queue(url):
    """
    Given a url, initiates a new message queue handler instance according to the url scheme
    :param url: url of the message queue
    :return: new message queue handler instance
    """
    url = furl(url)
    prefix = url.scheme
    if prefix not in config:
        raise ValueError("Message queue type is not supported")
    return config[prefix](url.host, url.port)


load_message_queues()
