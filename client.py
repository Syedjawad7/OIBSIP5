import socket

HEADER = 64
PORT = 5555
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Get the server's local IP address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def start():
    while True:
        message = input("Type a message (or type !q to exit): ")
        if message == "!q":
            send(DISCONNECT_MESSAGE)
            break
        send(message)


print("[CONNECTED] You are now connected to the server.")

start()
