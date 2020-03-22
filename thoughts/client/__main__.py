import click
from thoughts.client import client


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='8000')
def upload_sample(host, port):
    try:
        print("uploading sample")
        client.upload_sample(host, port)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='client')
