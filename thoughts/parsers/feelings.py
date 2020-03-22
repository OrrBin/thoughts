from thoughts.serializers.protobuf_serializer import ProtoBufSerializer

pbs = ProtoBufSerializer()


def parse_feelings(snapshot_bytes):
    snapshot = pbs.snapshot_decode(snapshot_bytes)
    feelings = dict(
        hunger=snapshot.feelings.hunger,
        thirst=snapshot.feelings.thirst,
        exhaustion=snapshot.feelings.exhaustion,
        happiness=snapshot.feelings.happiness)

    feelings = dict(feelings=feelings)

    return feelings


parse_feelings.identifier = 'feelings'
