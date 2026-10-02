# Terminal Communication

A simple Python socket-based two-player terminal game where one server manages the game flow and two clients connect to play in turns.

## Overview

This project demonstrates basic client-server communication using Python's `socket` module. The server listens for two clients, assigns each one a player number, and then handles turn-based interaction between them.

## Project Files

- `server.py` — creates the socket server, accepts connections, and manages the turn flow.
- `client.py` — connects to the server and sends/receives messages from the terminal.

## How it Works

1. The server starts and waits for two client connections.
2. Each client connects and receives a player assignment.
3. The server starts the game and tells players whose turn it is.
4. The active player enters a message in the terminal.
5. The server sends that move to the other player and continues the cycle.

## Requirements

- Python 3.x
- Two terminal sessions on the same machine, or a local network setup with both clients running on connected devices

## Running the Project

### 1. Start the server

Open a terminal in the project folder and run:

```bash
python server.py
```

### 2. Start the first client

Open a second terminal and run:

```bash
python client.py
```

### 3. Start the second client

Open a third terminal and run:

```bash
python client.py
```

This should connect both clients to the server and begin the game flow.

## Network Details

- Server port: `5050`
- Host address is determined dynamically using the local machine hostname.
- The project is intended for local testing and learning socket communication.

## Notes

- This is a learning/demo project, not a production-ready networking application.
- It is best suited for testing on the same machine or within the same local network.
- The server currently expects exactly two clients and keeps the game loop running until the program is terminated.

## Example Flow

```text
Server: "Hello, you are player 1"
Server: "Hello, you are player 2"
Server: "[Started Game] Let the battle, begin!"
Server: "Your turn"
Client 1: enters a message
Server: sends "Opponent played <message>" to Client 2
```
