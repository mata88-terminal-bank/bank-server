from constants import SIZE, FORMAT

def receive_client_request(server_client):
    conn, addr = server_client.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    """ Receiving the fault tolerance level for the file """
    request = conn.recv(SIZE).decode(FORMAT)
    print(
        f"[RECV] Receiving the request ({request}).")

    conn.send(
        f"Request received ({request}).".encode(FORMAT))
    return request, conn, addr
