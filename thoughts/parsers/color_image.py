from PIL import Image
from google.protobuf.message import DecodeError

from thoughts.core.context import Context
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer

pbs = ProtoBufSerializer()


def parse_color_image(snapshot_bytes, data_dir='/var/data/thoughts'):
    """
    Parsing color image data from snapshot. The image data itself is stored on disk, and the metadata returned
    """
    try:
        snapshot = pbs.snapshot_decode(snapshot_bytes)
    except DecodeError as e:
        print(e)
        raise e

    user_id = snapshot.user_id
    snapshot_id = snapshot.snapshot_id

    raw_data_path = snapshot.color_image.path
    size = snapshot.color_image.width, snapshot.color_image.height

    print(f'raw_data_path: {raw_data_path}, size: {size}')
    with open(raw_data_path, 'rb') as f:
        data = f.read()
    image = Image.frombytes('RGB', size, data)

    ctx = Context(f'{data_dir}/images', user_id, snapshot_id)
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
