import json

import click
import requests


def send_get_request(host, port, endpoint, is_binary=False):
    url = f'http://{host}:{port}/{endpoint}'
    response = requests.get(url=url)
    if not validate_response(response, is_binary):
        return None

    if is_binary:
        return response.content

    result = response.json()
    return json.dumps(result, indent=4)


def validate_response(response, is_binary):
    # message = 'error receiving binary response'
    # if not is_binary:

    status_code = response.status_code
    if status_code != 200:
        message = response.content.decode('utf-8')
        print(f'error occurred: {message} ({status_code})')
        return False

    return True


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
def get_users(host, port):
    result = send_get_request(host, port, 'users')
    if result:
        print(result)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
def get_user(host, port, user_id):
    result = send_get_request(host, port, f'users/{user_id}')
    if result:
        print(result)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
def get_snapshots(host, port, user_id):
    result = send_get_request(host, port, f'users/{user_id}/snapshots')
    if result:
        print(result)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(host, port, user_id, snapshot_id):
    result = send_get_request(host, port, f'users/{user_id}/snapshots/{snapshot_id}')
    if result:
        print(result)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.option('-s', '--save', default='')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result_name')
def get_result(host, port, save, user_id, snapshot_id, result_name):
    result = send_get_request(host, port, f'users/{user_id}/snapshots/{snapshot_id}/{result_name}')
    if not result:
        return

    if save:
        with open(save, 'w+') as f:
            f.write(result)
    else:
        print(result)


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='5000')
@click.argument('output_path')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result_name')
def get_result_data(output_path, host, port, user_id, snapshot_id, result_name):
    result = send_get_request(host, port, f'users/{user_id}/snapshots/{snapshot_id}/{result_name}/data',
                              is_binary=True)
    if not result:
        return

    with open(output_path, 'bw+') as f:
        f.write(result)


if __name__ == '__main__':
    cli(prog_name='cli')
