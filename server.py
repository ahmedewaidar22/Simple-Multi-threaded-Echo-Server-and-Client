# server.py

import socket
import threading

def handle_client(conn, addr):

    print(f"Connection from {addr}") 
    try:
        while True:
            data = conn.recv(1024)  
            if not data:
                print(f"Client {addr} disconnected")
                break
            message = data.decode('utf-8').strip()
            print(f"Received from {addr}: {message}")  
            if message.lower() == 'exit':
                print(f"Exit command received from {addr}. Closing connection.")
                break
            conn.sendall(data) 
            print(f"Sent to {addr}: {message}")  
    except ConnectionResetError:
      
        print(f"Connection with {addr} lost unexpectedly")
    finally:
        conn.close()

def main():
    HOST = '127.0.0.1' 
    PORT = 65432       
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen()  
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server_sock.accept() 
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True
        client_thread.start()

if __name__ == "__main__":
    main()
