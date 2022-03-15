# AMQP 1.0 PoC Service B
A test service for interacting with an AMQP 1.0 compliant broker.
Receives messages from the queue **poc-b**, modifies the message (assuming a defined contract defined in input_model.py)
and sends back a modified version on the **poc-a** queue.

## Docker Setup
#### Install Docker
`brew install --cask docker`

#### Create RabbitMQ Container
`docker-compose up -d`

If you run into the error: **filesystem layer verification failed for digest sha256**
then disable the VPN and execute the command.

## Install Required Services
#### Create a virtual environment
`python3 -m venv env`

#### Activate it
`source env/bin/activate`

#### Install qpid-proton
`pip3 install python-qpid-proton`


## Running the service
`./run_app.sh`

Ensure you are using your virtual env. This will spin up a qpid proton server that is ready to send/receive messages on the defined queues in the code.

## Viewing the Broker
Once the docker container is spun up, the broker will be running a management portal on localhost:15672.
The default user and password is guest/guest.
