import socket
import os
from client_connection import receive_client_request
from constants import CLIENT_ADDRESS, SIZE, FORMAT


def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the CLIENT_IP and CLIENT_PORT to the server_client. """
    server_client.bind(CLIENT_ADDRESS)

    """ Server is listening, i.e., server_client is now waiting for the client to connected. """
    server_client.listen()
    print("[LISTENING] Server is listening.")

    while True:
        request, conn, addr = receive_client_request(
            server_client)
        print("Received request is", request)

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        print("[LISTENING] Server is listening again.")


if __name__ == "__main__":
    main()
