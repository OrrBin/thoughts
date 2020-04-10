import os
import click
from thoughts.server import server


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='8000')
def run_server(host, port):

    mq_url = os.getenv('MQ_URL', 'rabbitmq://127.0.0.1:5672')
    try:
        print(f'mq url is: {mq_url}')
        server.run_server(host, port, mq_url=mq_url)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='server')
