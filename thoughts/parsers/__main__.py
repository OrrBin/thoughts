import os

import click
from . import parse as parse_data, run_one_parser
from . import run_parser as register_parser
from . import run_all_parsers


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
@click.argument('parser_name')
@click.option('--mq_url', default='rabbitmq://127.0.0.1:5672')
def run_parser(parser_name, mq_url):
    run_one_parser(parser_name, mq_url)


@cli.command()
def run_parsers():
    # If env variable is defined use it
    mq_url = os.getenv('MQ_URL', 'rabbitmq://127.0.0.1:5672')

    # If env variable is defined use it
    parser_to_run = os.getenv('PARSER', 'all')

    if parser_to_run == 'all':
        run_all_parsers(mq_url)
    else:
        run_one_parser(parser_to_run, mq_url)


if __name__ == '__main__':
    cli(prog_name='parsers')
