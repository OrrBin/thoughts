from flask import Flask, send_from_directory

app = Flask(__name__)


def run_gui_server(host, port):
    """
    Run web server that serves the Thoughts app.
    """
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
