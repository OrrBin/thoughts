from PIL import Image

from thoughts.core.context import Context
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

images_root_dir = '/var/data/thoughts/images'
pbs = ProtoBufSerializer()


def parse_color_image(snapshot_bytes):
    """
    Parsing color image data from snapshot. The image data itself is stored on disk, and the metadata returned
    """
    snapshot = pbs.snapshot_decode(snapshot_bytes)

    user_id = snapshot.user_id
    snapshot_id = snapshot.snapshot_id

    raw_data_path = snapshot.color_image.path
    size = snapshot.color_image.width, snapshot.color_image.height

    with open(raw_data_path, 'rb') as f:
        data = f.read()
    image = Image.frombytes('RGB', size, data)

    ctx = Context(images_root_dir, user_id, snapshot_id)
    file_path = ctx.path('color_image.jpg')
    file = open(file_path, 'w+')
    image.save(file)

    color_image = dict(
        width=size[0],
        height=size[1],
        path=file_path
    )

    return dict(color_image=color_image)


parse_color_image.identifier = 'color_image'
