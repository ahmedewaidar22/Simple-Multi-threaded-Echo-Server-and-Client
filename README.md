# 📡 Multi-threaded Echo Server and Client

A simple Python implementation of an echo server and client demonstrating IPv4 socket communication and threading.

## 🚀 Features

* **Echo Server (`server.py`)**

  * Uses IPv4 TCP sockets (`AF_INET`, `SOCK_STREAM`).
  * Runs on `127.0.0.1:65432` by default.
  * Accepts multiple client connections concurrently via `threading.Thread`.
  * Echoes back any message received until the client sends `exit`.
  * Logs connections, disconnections, and sent/received messages with client IP addresses.

* **Echo Client (`client.py`)**

  * Connects to the server on `127.0.0.1:65432`.
  * Reads user input from the command line.
  * Sends messages to the server and displays echoed responses.
  * Closes the connection gracefully when the user types `exit`.

## 📋 Requirements

* Python 3.x (tested on 3.8+)
* No external libraries required (built-in `socket` and `threading` modules).

## ⚙️ Setup & Usage

1. **Clone or download** this repository.

2. **Run the server** in one terminal:

   ```bash
   python server.py
   ```

   The server will start listening on `127.0.0.1:65432`.

3. **Run one or more clients** in separate terminals:

   ```bash
   python client.py
   ```

   * Enter messages at the prompt.
   * Type `exit` to disconnect the client.

4. **Observe logs** in the server terminal for connections, messages, and disconnections.

## 📝 Code Structure

```
├── server.py       # Multi-threaded echo server
├── client.py       # Echo client
└── README.md       # This documentation
```

### server.py Highlights

* **Socket Initialization**:

  ```python
  server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_sock.bind((HOST, PORT))
  server_sock.listen()
  ```
* **Thread-per-client**:

  ```python
  conn, addr = server_sock.accept()
  thread = threading.Thread(target=handle_client, args=(conn, addr))
  thread.start()
  ```
* **Echo Loop & Shutdown**:

  ```python
  data = conn.recv(1024)
  if message.lower() == 'exit':
      break
  conn.sendall(data)
  conn.close()
  ```

### client.py Highlights

* **Connect to Server**:

  ```python
  client_sock.connect((HOST, PORT))
  ```
* **Send & Receive**:

  ```python
  client_sock.sendall(message.encode('utf-8'))
  data = client_sock.recv(1024)
  ```

## ✅ Evaluation Criteria

1. **Proper IPv4 socket setup**: Uses `AF_INET`/`SOCK_STREAM` and correct binding/connecting.
2. **Effective threading**: Each client is handled in its own thread without blocking the main loop.
3. **Graceful shutdown**: Both server and clients detect `exit` and close sockets cleanly; handles disconnects and interrupts.
4. **Code clarity**: Well-documented with inline comments and clear log messages.

---

*Enjoy testing your multi-threaded echo application!*
