import click
from thoughts.server import server

_DATA_DIR = server.root_data_dir()


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='8000')
@click.option('-q', '--mq_url', default='rabbitmq://127.0.0.1:5672')
@click.option('-d', '--data_dir', default=_DATA_DIR)
def run_server(host, port, mq_url, data_dir):
    try:
        print(f'mq url is: {mq_url}')
        server.run_server(host, port, mq_url=mq_url, data_dir=data_dir)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='server')
