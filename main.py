import socket
import os
from constants import FORMAT
from client_connection import receive_client_request
from  create_database import start_db
from constants import CLIENT_ADDRESS, SIZE, FORMAT
from request_processor import process_request

from _thread import *
import threading

def threaded(conn, request, db_con, db_crsr):
  while True:
    
    # For every request received from the client side, we process it here
    msg = process_request(request, db_con, db_crsr)

    # Here we send the client a return message
    conn.send(msg.encode(FORMAT))

    # Closing the connection from the client. 
    conn.close()



def main():
    # Connecting to the database
    # The db connection and mysql cursor for db operations is initialized only once here
    # This is for economic reusage of this resource throughout every request operation
    db_con, db_crsr = start_db()
    print("Database initialized")

    # The following three commands are responsible for starting up the socket connection 
    print("[STARTING] Server is starting.")
    # Staring a TCP socket. 
    server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the CLIENT_IP and CLIENT_PORT to the server_client. 
    server_client.bind(CLIENT_ADDRESS)

    # Server is listening, i.e., server_client is now waiting for the client to connected. 
    server_client.listen()
    print("[LISTENING] Server is listening.")

    while True:
        request, conn, addr = receive_client_request(
            server_client)
        print("Received request is", request)

        start_new_thread(threaded, (conn, request, db_con, db_crsr))

        print(f"[DISCONNECTED] {addr} disconnected.")
        print("[LISTENING] Server is listening again.")


if __name__ == "__main__":
    main()
