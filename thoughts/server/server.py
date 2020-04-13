import json
import uuid

from ..core.thoughts_pb2 import Snapshot
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
from ..message_queues import init_queue

from thoughts.core.context import Context
from flask import Flask, request

_DATA_DIR = '/var/data/thoughts/data'

serv = Flask(__name__)
_data_dir = '/var/data/thoughts/data'
message_handler = None
url = None
protobuf_encoder = ProtoBufSerializer()


def run_server(host, port, mq_url=None, data_dir=_DATA_DIR):
    """
    Runs server that accepts snapshots, and distributes them to the given message queue.
    The Server saves the heavy data to files on disk, to prevent overloading the queue and network.
    :param mq_url: url to a message queue of a supported type
    :param data_dir: data directory
    """
    global _data_dir
    _data_dir = data_dir

    global url
    url = mq_url
    serv.run(host, int(port))


@serv.route('/snapshot', methods=['POST'])
def post_snapshot():
    message_bytes = request.get_data()
    user, enriched_snapshot = protobuf_encoder.message_decode(message_bytes)  # convert from bytes to pb objects

    snapshot_id = _create_id()

    color_image_data = enriched_snapshot.color_image.data
    depth_image_data = json.dumps(list(enriched_snapshot.depth_image.data))

    context = Context(_data_dir, user.user_id, snapshot_id)
    color_image_path = context.save('color_image', color_image_data)
    depth_image_path = context.save('depth_image', depth_image_data)

    print(f'saved color image at: {color_image_path}')
    print(f'saved depth image at: {depth_image_path}')

    snapshot = _flatten_snapshot(enriched_snapshot, snapshot_id, user.user_id, color_image_path, depth_image_path)

    if url:
        mq = init_queue(url)
        mq.publish('snapshot', protobuf_encoder.snapshot_encode(snapshot))
        mq.publish('user', _user_json(user))
    return "Success"


def _create_id():
    return str(uuid.uuid4())


def _user_json(user):
    return json.dumps(dict(
        user_id=user.user_id,
        username=user.username,
        birthday=user.birthday,
        gender=user.gender
    ))


def _flatten_snapshot(enriched_snapshot, snapshot_id, user_id, color_image_path, depth_image_path):
    """
    Gets an EnrichedSnapshot and create Snapshot object from it.
    """
    snapshot = Snapshot()
    snapshot.snapshot_id = snapshot_id
    snapshot.user_id = user_id
    snapshot.datetime = enriched_snapshot.datetime
    snapshot.pose.translation.x = enriched_snapshot.pose.translation.x
    snapshot.pose.translation.y = enriched_snapshot.pose.translation.y
    snapshot.pose.translation.z = enriched_snapshot.pose.translation.z

    snapshot.pose.rotation.x = enriched_snapshot.pose.rotation.x
    snapshot.pose.rotation.y = enriched_snapshot.pose.rotation.y
    snapshot.pose.rotation.z = enriched_snapshot.pose.rotation.z
    snapshot.pose.rotation.w = enriched_snapshot.pose.rotation.w

    snapshot.feelings.hunger = enriched_snapshot.feelings.hunger
    snapshot.feelings.thirst = enriched_snapshot.feelings.thirst
    snapshot.feelings.exhaustion = enriched_snapshot.feelings.exhaustion
    snapshot.feelings.happiness = enriched_snapshot.feelings.happiness

    snapshot.color_image.width = enriched_snapshot.color_image.width
    snapshot.color_image.height = enriched_snapshot.color_image.height
    snapshot.color_image.path = color_image_path

    snapshot.depth_image.width = enriched_snapshot.depth_image.width
    snapshot.depth_image.height = enriched_snapshot.depth_image.height
    snapshot.depth_image.path = depth_image_path

    return snapshot
