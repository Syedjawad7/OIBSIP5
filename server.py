import socket
import threading

# Server configuration
HEADER = 64
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive the message length
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Receive the actual message
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DISCONNECTED] {addr} disconnected.")
            else:
                print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Accept a new connection
        conn, addr = server.accept()
        # Create a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()
