from proton import Url
from proton.reactor import Container

from app.handler import Handler

url = Url('localhost:5672/poc-b')
# Create an AMQP container (link) on the given url and run the handler
Container(Handler(url)).run()
