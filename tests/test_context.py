import os.path
from thoughts.core.context import Context

_USER_ID = 'test_user_id'
_SNAPSHOT_ID = 'test_snapshot_id'
_FILENAME = 'test_name'
_FILE_DATA = 'data'


def test_context():
    ctx = Context('.', _USER_ID, _SNAPSHOT_ID)
    file_path = ctx.path(_FILENAME)
    assert file_path == f'./{_USER_ID}/{_SNAPSHOT_ID}/{_FILENAME}'

    file_path = ctx.save(_FILENAME, _FILE_DATA)
    assert os.path.isfile(file_path)
    with open(file_path, 'r') as f:
        assert f.readline() == _FILE_DATA

    os.remove(file_path)
