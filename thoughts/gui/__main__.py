import click
from thoughts.gui import run_gui_server


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5555')
@click.option('-a', '--api_url')
def run_server(host, port, api_url):
    """
    Starts web server that serves the Thoughts app.
    """

    try:
        run_gui_server(host, port, api_url)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='gui')
