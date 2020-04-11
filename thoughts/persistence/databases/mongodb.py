import pymongo

# docker run -d -p 27017:27017 -v ~/data:/data/db mongo

DB = "thoughts"
USERS_COL = "users"
SNAPSHOT_COL = "snapshots"


class MongoDB:
    """
    Driver for MongoDB
    """
    prefix = 'mongodb'

    def __init__(self, host, port):
        self.address = f'{host}:{port}'
        self.client = pymongo.MongoClient(f'mongodb://{self.address}')
        self.db = self.client[DB]
        self.users = self.db[USERS_COL]
        self.snapshots = self.db[SNAPSHOT_COL]

    def __repr__(self):
        return f'MongoDB({self.address})'

    # Retrieves
    def get_users(self):
        return self.users.find()

    def get_user_by_id(self, user_id):
        return self.users.find_one({'user_id': user_id})

    def get_snapshot_by_id(self, user_id, snapshot_id):
        return self.snapshots.find_one({'user_id': user_id, 'snapshot_id': snapshot_id})

    def get_snapshots_by_user_id(self, user_id):
        return self.snapshots.find({'user_id': user_id})

    # Updates
    def update_user(self, user, upsert=True):
        self.users.update_one({'user_id': user['user_id']}, {
                '$set': user
            }, upsert=upsert)

    def update_snapshot(self, snapshot_id, data, upsert=True):
        updates = dict()
        for (majorkey, majorSubDict) in data.items():
            if not isinstance(majorSubDict, dict):
                updates[majorkey] = majorSubDict

        fields = data['data']
        for (majorkey, majorSubDict) in fields.items():
            if not isinstance(majorSubDict, dict):
                updates[majorkey] = majorSubDict

            else:
                updates[majorkey] = dict()
                for (minorkey, minorSubDict) in majorSubDict.items():
                    updates[majorkey][minorkey] = minorSubDict

        if type(data) == dict:
            self.snapshots.update_one({'snapshot_id': snapshot_id}, {
                '$set': updates
            }, upsert=upsert)
