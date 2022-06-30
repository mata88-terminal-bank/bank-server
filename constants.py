import socket

CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_PORT = 4455
CLIENT_ADDRESS = (CLIENT_IP, CLIENT_PORT)

SIZE = 1024
FORMAT = "utf-8"
