import os
import sys

import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from thoughts.core.thoughts_pb2 import Snapshot
from thoughts.core.thoughts_pb2 import EnrichedSnapshot
from thoughts.core.thoughts_pb2 import User

number_of_image_sets = 5


def get_test_users(num=10):
    for i in range(0, num):
        user = User()
        id = random.randint(1, 100)
        user.user_id = id
        user.username = f'test_user_{id}'
        user.birthday = random.randint(0, 10000)
        user.gender = random.randint(0, 2)

        yield user


def get_test_snapshots(num=10):
    for i in range(0, num):
        snapshot = Snapshot()
        snapshot.snapshot_id = 'testId'
        snapshot.user_id = random.randint(1, 100)
        snapshot.datetime = random.randint(0, 10000)
        snapshot.pose.translation.x = random.random()
        snapshot.pose.translation.y = random.random()
        snapshot.pose.translation.z = random.random()

        snapshot.pose.rotation.x = random.random()
        snapshot.pose.rotation.y = random.random()
        snapshot.pose.rotation.z = random.random()
        snapshot.pose.rotation.w = random.random()

        snapshot.feelings.hunger = random.random()
        snapshot.feelings.thirst = random.random()
        snapshot.feelings.exhaustion = random.random()
        snapshot.feelings.happiness = random.random()

        snapshot.color_image.width = 1920
        snapshot.color_image.height = 1080
        snapshot.color_image.path = f'./tests/assets/assets_{random.randint(1, number_of_image_sets)}/color_image'

        snapshot.depth_image.width = 224
        snapshot.depth_image.height = 172
        snapshot.depth_image.path = f'./tests/assets/assets_{random.randint(1, number_of_image_sets)}/depth_image'

        yield snapshot


def get_test_messages(num=10):
    for i in range(0, num):
        user_id = random.randint(1, 100)

        snapshot = Snapshot()
        snapshot.snapshot_id = 'testId'
        snapshot.user_id = user_id
        snapshot.datetime = random.randint(0, 10000)
        snapshot.pose.translation.x = random.random()
        snapshot.pose.translation.y = random.random()
        snapshot.pose.translation.z = random.random()

        snapshot.pose.rotation.x = random.random()
        snapshot.pose.rotation.y = random.random()
        snapshot.pose.rotation.z = random.random()
        snapshot.pose.rotation.w = random.random()

        snapshot.feelings.hunger = random.random()
        snapshot.feelings.thirst = random.random()
        snapshot.feelings.exhaustion = random.random()
        snapshot.feelings.happiness = random.random()

        snapshot.color_image.width = 1920
        snapshot.color_image.height = 1080
        snapshot.color_image.path = f'./tests/assets/assets_{random.randint(1, number_of_image_sets)}/color_image'

        snapshot.depth_image.width = 224
        snapshot.depth_image.height = 172
        snapshot.depth_image.path = f'./tests/assets/assets_{random.randint(1, number_of_image_sets)}/depth_image'

        user = User()
        user.user_id = user_id
        user.username = f'test_user_{user_id}'
        user.birthday = random.randint(0, 10000)
        user.gender = random.randint(0, 2)

        yield user, snapshot
