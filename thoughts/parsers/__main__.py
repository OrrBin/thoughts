import click
from . import parse as parse_data, run_one_parser
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
@click.argument('parser')
@click.option('--mq_url', default='rabbitmq://127.0.0.1:5672')
def run_parser(parser, mq_url):
    run_one_parser(parser, mq_url)


@cli.command()
@click.option('-p', '--parser', default='all')
@click.option('-q', '--mq_url', default='rabbitmq://127.0.0.1:5672')
def run_parsers(parser, mq_url):
    if parser == 'all':
        run_all_parsers(mq_url)
    else:
        run_one_parser(parser, mq_url)


if __name__ == '__main__':
    cli(prog_name='parsers')
