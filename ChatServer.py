import Message_pb2


class ChatAppServicer(Message_pb2):
    def __init__(self, db):
        self.db = db

