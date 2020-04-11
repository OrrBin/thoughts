import json
from thoughts.persistence.databases import init_database
from thoughts.message_queues import init_queue
from thoughts.parsers import get_available_parsers
from threading import Thread


class Saver:
    """
    Saver for user and snapshot data.
    Relies on database driver, creating one using the database_url
    Consumes message queue for snapshots and user updates
    """
    def __init__(self, database_url):
        self.db = init_database(database_url)

    def save(self, topic, data):
        print(f'Saving data for topic: {topic}')
        data = json.loads(data)
        self.db.update_snapshot(data['snapshot_id'], data)

    def save_user(self, user):
        user = json.loads(user)
        self.db.update_user(user)

    def run_saver(self, parser_name, mq_url):
        mq = init_queue(mq_url)
        mq.consume(parser_name, lambda body: self.save(parser_name, body))

    def run_user_saver(self, mq_url):
        mq = init_queue(mq_url)
        mq.consume('user', lambda body: self.save_user(body))

    def run_all_savers(self, mq_url):
        # Listen to users updates
        t = Thread(target=self.run_user_saver, args=(mq_url,))
        t.start()
        print(f'Listening to: user')

        # Listen to parsers updates
        for parser_name in get_available_parsers():
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
            print(f'Listening to: {parser_name}')
