import zmq

context = zmq.Context()
socket_server = context.socket(zmq.DEALER)
socket_client = context.socket(zmq.DEALER)

socket_server.bind("tcp://*:5556")
socket_client.connect("tcp://localhost:5555")

poller = zmq.Poller()
poller.register(socket_server, zmq.POLLIN)
poller.register(socket_client, zmq.POLLIN)

while True:
    socks = dict(poller.poll())
    if socket_server in socks and socks[socket_server] == zmq.POLLIN:
        message = socket_server.recv_string()
        print(f"{message}")
        break

context.destroy()