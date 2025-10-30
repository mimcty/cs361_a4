import zmq

context = zmq.Context()
socket_server = context.socket(zmq.DEALER)
socket_client = context.socket(zmq.DEALER)

socket_server.bind("tcp://*:5555")
socket_client.connect("tcp://localhost:5556")

poller = zmq.Poller()
poller.register(socket_server, zmq.POLLIN)
poller.register(socket_client, zmq.POLLIN)

socket_client.send_string("This is a message from CS361.")

context.destroy()