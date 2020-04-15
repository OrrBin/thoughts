import json
import datetime as dt

from thoughts.core.context import Context
from thoughts.utils.serializers.protobuf_serializer import ProtoBufSerializer
import numpy as np

import matplotlib.pyplot as plt

# heatmaps_root_dir = '/var/data/thoughts/heatmaps'
pbs = ProtoBufSerializer()


def parse_depth_image(snapshot_bytes, data_dir='/var/data/thoughts'):
    """
    Parsing depth image data from snapshot. The image data itself is stored on disk, and the metadata returned
    """
    snapshot = pbs.snapshot_decode(snapshot_bytes)

    user_id = snapshot.user_id
    snapshot_id = snapshot.snapshot_id
    timestamp = snapshot.datetime
    time_str = dt.datetime.fromtimestamp(timestamp / 1000).strftime("%d/%m/%y %H:%M:%S")

    raw_data_path = snapshot.depth_image.path
    width, height = snapshot.depth_image.width, snapshot.depth_image.height
    size = (height, width)
    with open(raw_data_path, 'r') as f:
        data = f.read()

    data = json.loads(data)
    shaped = np.reshape(data, size)

    ctx = Context(f'{data_dir}/heatmaps', user_id, snapshot_id)
    heatmap_path = ctx.path('heatmap.png')

    # Plot heatmap
    plt.clf()
    plt.title(f'heatmap from {time_str}')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.imshow(shaped, interpolation='nearest')
    plt.savefig(heatmap_path)
    depth_image = dict(
        width=width,
        height=height,
        path=heatmap_path
    )

    return dict(depth_image=depth_image)


parse_depth_image.identifier = 'depth_image'
