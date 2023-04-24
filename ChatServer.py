class ChatAppServicer(Message_pb2_grpc.ChatAppServicer):
    def __init__(self, db):
        self.db = db


    