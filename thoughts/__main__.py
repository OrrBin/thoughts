# import click
#
# from thoughts.serializers.protobuf_serializer import ProtoBufSerializer
# from thoughts.file_reader.file_reader import FileReader
# from thoughts.client import client
# from thoughts.server import server
# from thoughts.message_queues import init_queue
#
#
# @click.group()
# def cli():
#     pass
#
#
# @cli.command()
# @click.option('--path', default='./sample.mind.gz')
# @click.argument('size', type=int)
# def read(path, size):
#     reader = FileReader(path)
#     for i in range(size):
#         print(reader.get_snapshot())
#     reader.close()
#
#
# @cli.command()
# @click.option('-h', '--host', default='127.0.0.1')
# @click.option('-p', '--port', default='8000')
# @click.option('--path', default='./sample.mind.gz')
# def upload_sample(host, port, path):
#     print("uploading")
#     client.upload_sample(host, port, path)
#
#
# @cli.command()
# @click.option('-h', '--host', default='127.0.0.1')
# @click.option('-p', '--port', default='8000')
# def run_server(host, port):
#     try:
#         server.run_server(host, port, mq_url="rabbitmq://127.0.0.1:5672")
#     except Exception as error:
#         print(f'ERROR: {error}')
#
#
# @cli.command()
# def run_parser():
#     mq = init_queue('rabbitmq://127.0.0.1:5672')
#     mq.consume('snapshot', callback)
#
#
# def callback(body):
#     encoder = ProtoBufSerializer()
#     snap = body
#     print(snap)
#     print(type(snap))
#     print("\n\n\n")
#     snap = encoder.snapshot_decode(snap)
#     print(snap)
#     print(type(snap))
#     print("\n\n\n")
#     # snap = encoder.snapshot_decode(snap)
#     # print(snap)
#     # print(type(snap))
#     # print("\n\n\n")
#
#     # print(snap["timestamp"])
#     # print("finish")
#
#
# if __name__ == '__main__':
#     cli(prog_name='thoughts')
