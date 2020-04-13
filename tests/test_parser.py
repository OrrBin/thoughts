from thoughts.parsers.color_image import parse_color_image
from thoughts.parsers.depth_image import parse_depth_image
from thoughts.parsers.feelings import parse_feelings
from thoughts.parsers.pose import parse_pose
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

from PIL import Image

from tests.conftest import get_test_snapshots

number_of_test_cases = 10


def test_parse_color_image():
    for snapshot in get_test_snapshots(number_of_test_cases):
        serializer = ProtoBufSerializer()
        snapshot_bytes = bytes(serializer.snapshot_encode(snapshot))

        result = parse_color_image(snapshot_bytes)

        result = result['color_image']
        assert result['width'] == snapshot.color_image.width
        assert result['height'] == snapshot.color_image.height

        image_path = result['path']
        image = Image.open(image_path)
        created_width, created_height = image.size

        assert created_width == snapshot.color_image.width
        assert created_height == snapshot.color_image.height


def test_parse_depth_image():
    for snapshot in get_test_snapshots(number_of_test_cases):
        serializer = ProtoBufSerializer()
        snapshot_bytes = bytes(serializer.snapshot_encode(snapshot))

        result = parse_depth_image(snapshot_bytes)

        result = result['depth_image']
        assert result['width'] == snapshot.depth_image.width
        assert result['height'] == snapshot.depth_image.height

        image_path = result['path']
        image = Image.open(image_path)

        assert image


def test_parse_feelings():
    for snapshot in get_test_snapshots(number_of_test_cases):
        serializer = ProtoBufSerializer()
        snapshot_bytes = bytes(serializer.snapshot_encode(snapshot))

        result = parse_feelings(snapshot_bytes)
        result = result['feelings']

        assert result['hunger'] == snapshot.feelings.hunger
        assert result['thirst'] == snapshot.feelings.thirst
        assert result['exhaustion'] == snapshot.feelings.exhaustion
        assert result['happiness'] == snapshot.feelings.happiness


def test_parse_pose():
    for snapshot in get_test_snapshots(number_of_test_cases):
        serializer = ProtoBufSerializer()
        snapshot_bytes = bytes(serializer.snapshot_encode(snapshot))

        result = parse_pose(snapshot_bytes)
        result = result['pose']

        assert result['translation']['x'] == snapshot.pose.translation.x
        assert result['translation']['y'] == snapshot.pose.translation.y
        assert result['translation']['z'] == snapshot.pose.translation.z

        assert result['rotation']['x'] == snapshot.pose.rotation.x
        assert result['rotation']['y'] == snapshot.pose.rotation.y
        assert result['rotation']['z'] == snapshot.pose.rotation.z
        assert result['rotation']['w'] == snapshot.pose.rotation.w

