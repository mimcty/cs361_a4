import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send_string("Send message")
message = socket.recv().decode('utf-8')

print(f"{message}")
socket.send_string("Q")         # send Q so server quits and stops listening for requests