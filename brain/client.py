from .thought import Thought
from .utils.connection import Connection
import datetime as dt


def upload_thought(address, user, thought):
    """
    Sends the specified thought, with the timestamp and user, to the specified address
    :param address: the address to send the thought to
    :param user: the user who send the thought
    :param thought: the thought content
    """
    conn = Connection.connect(*address)

    with conn:
        thought = Thought(user, dt.datetime.now(), thought)
        conn.send(thought.serialize())
