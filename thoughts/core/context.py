import os


class Context:
    """
    Defines a snapshot specific context
    Exposes functionality to save files, and create paths related to the specific snapshot
    """
    def __init__(self, data_dir, user_id, snapshot_id):
        self.data_dir = f'{data_dir}/{user_id}/{snapshot_id}'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save(self, name, data):
        """
        Save file in this context, in a subdirectory of this context data_dir
        :param name: file name
        :param data: file data
        :return: path to the created file
        """
        path = self.path(name)
        mode = 'wb+' if type(data) == bytes else 'w+'
        with open(path, mode) as f:
            f.write(data)
        return path

    def path(self, name):
        return f'{self.data_dir}/{name}'
