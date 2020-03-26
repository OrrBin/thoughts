from flask import Flask, jsonify, send_file
from thoughts.persistence.databases import init_database

api_server = Flask(__name__)
db = None


def run_api_server(host, port, database_url):
    global db
    db = init_database(database_url)
    print('starting api...')
    api_server.run(host, int(port))


@api_server.route('/users', methods=['GET'])
def get_users():
    users = db.get_users()
    users = [{'user_id': user['user_id'], 'username': user['username']} for user in users]
    return jsonify(users)


@api_server.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = db.get_user_by_id(user_id)
    user = {'user_id': user['user_id'], 'username': user['username'], 'birthday': user['birthday'],
            'gender': user['gender']}
    return jsonify(user)


@api_server.route('/users/<int:user_id>/snapshots')
def get_snapshots_by_user_id(user_id):
    snapshots = db.get_snapshots_by_user_id(user_id)
    snapshots = [{'snapshot_id': snapshot['snapshot_id'], 'date': snapshot['timestamp']}
                 for snapshot in snapshots]
    return jsonify(snapshots)


@api_server.route('/users/<int:user_id>/snapshots/<snapshot_id>')
def get_snapshot_by_id(user_id, snapshot_id):
    results = list()
    snapshot = db.get_snapshot_by_id(user_id, snapshot_id)
    for key in snapshot.keys():
        if isinstance(snapshot[key], dict):
            results.append(key)

    return jsonify(results)


@api_server.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>')
def get_snapshot_result(user_id, snapshot_id, result_name):
    try:
        result = db.get_snapshot_by_id(user_id, snapshot_id)[result_name]
    except:
        return f'unknown result : {result_name}', 400

    if not isinstance(result, dict):
        return f'unknown result : {result_name}', 400

    return jsonify(result)


@api_server.route('/users/<int:user_id>/snapshots/<snapshot_id>/<result_name>/data')
def get_snapshot_result_data(user_id, snapshot_id, result_name):
    result = None
    try:
        result = db.get_snapshot_by_id(user_id, snapshot_id)[result_name]
    except:
        return f'unknown result : {result_name}', 400

    try:
        path = result['path']
    except:
        return f'data for result {result_name} not found', 400

    return send_file(path)
