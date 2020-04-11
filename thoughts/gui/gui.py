from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from thoughts.persistence.databases import init_database

app = Flask(__name__)
CORS(app)


def run_api_server(host, port, database_url):
    print('starting gui...')
    app.run(host, int(port))
