from flask import Flask, send_from_directory
import os
from os import path

app = Flask(__name__)


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


def run_gui_server(host, port, api_url=None):
    """
    Starts web server that serves the Thoughts app.
    If API_URL environment variable exists, updates the configuration of the app to use this url using
    the update_api_url function
    """

    if api_url:
        update_api_url(api_url)

    print('Serving Thoughts App...')
    app.run(host, int(port))


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    if path.endswith('.js'):
        return send_from_directory('./static', path, mimetype='application/javascript')
    return send_from_directory('./static', path)


@app.route('/')
def root():
    return send_from_directory('./static', 'index.html')


@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred [main.py] %s' % e, 500
