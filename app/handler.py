from proton import Message
from proton.handlers import MessagingHandler

from app.input_model import InputModel


class Handler(MessagingHandler):
    # Constructor
    def __init__(self, url):
        super(Handler, self).__init__()
        self.url = url
        self.queue = url.path

    # Called when the container is created
    # Establishes a connection to the broker
    # Then declares this handler as a sender on the 'poc-a' queue and receiver
    def on_start(self, event):
        print("Listening on", self.url)
        self.container = event.container
        self.conn = event.container.connect(self.url)
        self.receiver = event.container.create_receiver(self.conn, self.queue)
        self.sender = event.container.create_sender(self.conn, 'poc-a')

    # Called when a message is received
    # Converts the incoming message to a pydantic input model and sends back a modified version
    # on the defined sender queue above (poc-a)
    def on_message(self, event):
        print("Received", event.message.body)
        new_body = InputModel.parse_raw(event.message.body)
        new_body.message = "I changed the message"
        self.sender.send(Message(body=new_body.json(),
                                 correlation_id=event.message.correlation_id))


