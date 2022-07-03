from constants import SIZE, FORMAT

# Receives socket connection from the client and decodes the received request string
def receive_client_request(server_client):
    conn, addr = server_client.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    """ Receiving the request for the file """
    request = conn.recv(SIZE).decode(FORMAT)
    print(
        f"[RECV] Receiving the request ({request}).")

    return request, conn, addr
