import click
from . import parse as parse_data, run_one_parser
from . import run_all_parsers

from thoughts.server import server

_DATA_DIR = server.root_data_dir()

@click.group()
def cli():
    pass


@cli.command()
@click.argument('parser_name')
@click.argument('path')
def parse(parser_name, path):
    with open(path, 'r') as f:
        result = parse_data(parser_name, f.read())
    print(result)


@cli.command()
@click.argument('parser')
@click.option('--mq_url', default='rabbitmq://127.0.0.1:5672')
@click.option('-d', '--data_dir', default=_DATA_DIR)
def run_parser(parser, mq_url, data_dir):
    run_one_parser(parser, mq_url, data_dir)


@cli.command()
@click.option('-p', '--parser', default='all')
@click.option('-q', '--mq_url', default='rabbitmq://127.0.0.1:5672')
@click.option('-d', '--data_dir', default=_DATA_DIR)
def run_parsers(parser, mq_url, data_dir):
    if parser == 'all':
        run_all_parsers(mq_url, data_dir)
    else:
        run_one_parser(parser, mq_url, data_dir)


if __name__ == '__main__':
    cli(prog_name='parsers')
