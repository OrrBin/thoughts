import os
from os import path

import click
from thoughts.gui import run_gui_server


@click.group()
def cli():
    pass


def update_api_url(api_url):
    """
    The Thoughts app is using the ./static/env.js file as configuration file.
    This function updates the api url in this file to the given url.
    """
    base_path = path.dirname(__file__)
    file_path = path.abspath(path.join(base_path, "static", "env.js"))

    data = ''
    with open(file_path, 'r') as fin:
        for line in fin:
            if 'apiUrl' in line:
                equals_index = line.index('=')
                new_line = line[0:equals_index + 1]
                new_line += f" '{api_url}'\n"
                data += new_line
            else:
                data += line

    with open(file_path, 'w') as fout:
        fout.write(data)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5555')
def run_server(host, port):
    """
    Starts web server that serves the Thoughts app.'
    If API_URL environment variable exists, updates the configuration of the app to use this url using
    the update_api_url function
    """
    # If env variable is defined use it
    api_url = os.getenv('API_URL')
    if api_url:
        update_api_url(api_url)

    try:
        run_gui_server(host, port)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='gui')
