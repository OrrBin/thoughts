# import datetime as dt
#
#
# class Snapshot:
#     def __init__(self, user_id, snapshot_id, timestamp, pose, color_image_path, color_image_width, color_image_height,
#                  depth_image_path, depth_image_width, depth_image_height, feelings):
#         self.user_id = user_id
#         self.timestamp = timestamp
#         self.snapshot_id = snapshot_id
#         self.pose = pose
#         self.color_image_path = color_image_path
#         self.color_image_width = color_image_width
#         self.color_image_height = color_image_height
#         self.depth_image_path = depth_image_path
#         self.depth_image_width = depth_image_width
#         self.depth_image_height = depth_image_height
#         self.feelings = feelings
#
#     def __repr__(self):
#         date = self.time_str()
#         translation = [float("%0.1f" % self.pose.translation.x), float("%0.1f" % self.pose.translation.y),
#                        float("%0.1f" % self.pose.translation.z)]
#         rotation = [float("%0.1f" % self.pose.rotation.x), float("%0.1f" % self.pose.rotation.y),
#                     float("%0.1f" % self.pose.rotation.z), float("%0.1f" % self.pose.rotation.w)]
#         hunger = float("%0.1f" % self.feelings.hunger)
#         thirst = float("%0.1f" % self.feelings.thirst)
#         exhaustion = float("%0.1f" % self.feelings.exhaustion)
#         happiness = float("%0.1f" % self.feelings.happiness)
#
#         line1 = f'{date=}, {translation=}, {rotation=}'
#         line2 = f'\t\t {hunger=}, {thirst=}, {exhaustion=}, {happiness=}'
#         return f'Snapshot({line1}\n{line2})'
#
#     def __str__(self):
#         date = self.time_str()
#         translation = [float("%0.1f" % self.pose.translation.x), float("%0.1f" % self.pose.translation.y),
#                        float("%0.1f" % self.pose.translation.z)]
#         rotation = [float("%0.1f" % self.pose.rotation.x), float("%0.1f" % self.pose.rotation.y),
#                     float("%0.1f" % self.pose.rotation.z), float("%0.1f" % self.pose.rotation.w)]
#         ci_size = f'{self.color_image_height}x{self.color_image_width}'
#         di_size = f'{self.depth_image_height}x{self.depth_image_width}'
#         line1 = f'Snapshot from {date} on {translation} / {rotation}'
#         line2 = f'with a {ci_size} color image and a {di_size} width image.'
#         return f'{line1} {line2}'
#
#     def time_str(self):
#         return dt.datetime.fromtimestamp(self.timestamp / 1000).strftime("%d/%m/%y")
