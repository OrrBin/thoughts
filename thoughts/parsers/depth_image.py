import json

from thoughts.serializers.protobuf_serializer import ProtoBufSerializer
import numpy as np

import matplotlib.pyplot as plt

images_root_dir = '/home/user/thoughts/images'
pbs = ProtoBufSerializer()


def parse_depth_image(snapshot_bytes):
    snapshot = pbs.snapshot_decode(snapshot_bytes)

    raw_data_path = snapshot.depth_image.path
    width, height = snapshot.depth_image.width, snapshot.depth_image.height
    size = (width, height)
    with open(raw_data_path, 'r') as f:
        data = f.read()

    data = json.loads(data)
    shaped = np.reshape(data, size)

    # Create heatmap
    # heatmap, xedges, yedges = np.histogram2d(shaped)
    # extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    # Plot heatmap
    plt.clf()
    plt.title('heatmap')
    plt.ylabel('y')
    plt.xlabel('x')
    # plt.imshow(heatmap, extent=extent)
    plt.imshow(shaped, cmap='hot', interpolation='nearest')
    plt.show()

    depth_image = dict(
        width=width,
        height=height,
        path=raw_data_path
    )

    return dict(depth_image=depth_image)


parse_depth_image.identifier = 'depth_image'
