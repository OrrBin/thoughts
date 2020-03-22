import json
from thoughts.persistence.databases import init_database
from thoughts.message_queues import init_queue
from thoughts.parsers import get_available_parsers
from threading import Thread


class Saver:
    def __init__(self, database_url):
        self.db = init_database(database_url)

    def save(self, topic, data):
        print(f'Saving for topic: {topic}')
        data = json.loads(data)
        print(data)
        if topic == 'user':
            self.db.insert_user(data)
        else:
            self.db.update_snapshot(data['snapshot_id'], data)

    def run_saver(self, parser_name, mq_url):
        mq = init_queue(mq_url)
        mq.consume(parser_name, lambda body: self.save(parser_name, body))

    def run_all_savers(self, mq_url):
        for parser_name in get_available_parsers():
            t = Thread(target=self.run_saver, args=(parser_name, mq_url))
            t.start()
            print(f'Now listening on exchange: {parser_name}')





