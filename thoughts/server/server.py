import json
import uuid

from ..core.thoughts_pb2 import Snapshot
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
from ..message_queues import init_queue

from thoughts.core.context import Context
from flask import Flask, request

serv = Flask(__name__)
data_dir = '/home/user/thoughts/data'
message_handler = None
url = None
protobuf_encoder = ProtoBufSerializer()


def run_server(host, port, publish=None, mq_url=None):
    if publish:
        global message_handler
        message_handler = publish
    else:
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

    context = Context(data_dir, user.user_id, snapshot_id)
    color_image_path = context.save('color_image', color_image_data)
    depth_image_path = context.save('depth_image', depth_image_data)

    snapshot = _flatten_snapshot(enriched_snapshot, snapshot_id, user.user_id, color_image_path, depth_image_path)

    if message_handler:  # run_server was invoked through API
        message_handler(message_bytes)
        return ""  # return status code 200

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
