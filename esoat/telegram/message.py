class Message:
    def __init__(self, **data):
        self.chat_id = data.get('message_id')
        self.author = data.get('from', None)
        self.sender_chat = data.get('sender_chat', None)
