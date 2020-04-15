import importlib
import sys
from furl import furl
from pathlib import Path

config = {}


def load_databases():
    """
    Collects database drivers and registers them.
    Registers according to their prefix attribute.
    For example for drivers with prefix attribute equals to mongodb
    It would be registered under mongodb.

    To add a new driver add a file, with name that end with db.py, implement the driver and add prefix attribute
    with the specific database type.
    The driver must implement the all the functions that mongodb.py implements

    And have a constructor accepting: host, port
    """
    root = Path(__file__).parent.absolute()
    sys.path.insert(0, str(root.parent))
    for file in root.iterdir():
        if file.name.startswith('_') or not file.suffix == '.py':
            continue
        module = importlib.import_module(f'{root.name}.{file.stem}', package=root.name)

        for key, db in module.__dict__.items():
            if isinstance(db, type) and db.__name__.endswith("DB"):
                config[db.prefix] = db


def init_database(url):
    url = furl(url)
    prefix = url.scheme
    if prefix not in config:
        raise ValueError("Database type is not supported")
    return config[prefix](url.host, url.port)


load_databases()
