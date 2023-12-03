# Simple Chat Application

This is a basic chat application implemented in Python using socket programming. The application consists of a server that listens for incoming connections and multiple clients that can send messages to the server.

## Getting Started

### Prerequisites

- Python 3
- `pip install threading`

### Running the Server

1. Open a terminal and navigate to the server directory.
2. Run the following command to start the server:

    ```bash
    python server.py
    ```

   The server will start listening for incoming connections.

### Running the Client

1. Open a new terminal window and navigate to the client directory.
2. Run the following command to start the client:

    ```bash
    python client.py
    ```

   You will be prompted to type a message. Type your message and press Enter to send it to the server.

   To disconnect from the server, type `!q` and press Enter.

## How It Works

- The server listens for incoming connections on a specified port.
- Each client connects to the server and can send messages.
- The server broadcasts received messages to all connected clients.
- To disconnect from the server, the client sends the `!q` command.

## Customization

Feel free to customize the code according to your requirements. You can modify the server and client scripts to add more features or change the communication protocol.
