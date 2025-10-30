import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")

    if len(message) > 0:
        if message.decode() == 'Q':
            break

        send_message = "This is a message from CS361."
        socket.send_string(send_message)

context.destroy()