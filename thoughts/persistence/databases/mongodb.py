import pymongo

# docker run -d mongo
# docker run -d -p 27017:27017 -v ~/data:/data/db mongo
# docker run -d -p 27017:27017 mongo

DB = "thoughts"
USERS_COL = "users"
SNAPSHOT_COL = "snapshots"


class MongoDB:
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
        return self.users.find({'id': user_id})

    def get_snapshot_by_id(self, snapshot_id):
        return self.snapshots.find({'snapshot_id': snapshot_id})

    def get_snapshot_by_user_id(self, user_id):
        return self.snapshots.find({'user_id': user_id})

    # Updates
    def insert_user(self, user):
        self.users.insert_one(user)

    def insert_snapshot(self, topic, data):
        if type(data) == dict:
            self.snapshots.insert_one({'topic': topic, **data})

        if type(data) == str:
            self.snapshots.insert_one({'name': topic, 'data': data})

    def update_snapshot(self, snapshot_id, data, upsert=True):

        print(data)

        updates = dict()
        for (majorkey, majorSubDict) in data.items():
            if majorkey == 'snapshot_id' or majorSubDict is str:
                continue

            updates[majorkey] = dict()
            for (minorkey, minorSubDict) in majorSubDict.items():
                updates[majorkey][minorkey] = minorSubDict

        print(updates)

        if type(data) == dict:
            self.snapshots.update_one({'snapshot_id': snapshot_id}, {
                '$set': updates
            }, upsert=upsert)
