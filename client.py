# client.py

import socket

def main():
    HOST = '127.0.0.1' 
    PORT = 65432       
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
    try:
        while True:
            message = input("Enter message (type 'exit' to quit): ")
            client_sock.sendall(message.encode('utf-8'))
            if message.lower() == 'exit':
                print("Closing connection.")
                break
            data = client_sock.recv(1024)
            if not data:
                print("Server closed the connection.")
                break
            print("Received from server:", data.decode('utf-8'))
    except KeyboardInterrupt:
        print("\nClient interrupted. Closing connection.")
    finally:
        client_sock.close()

if __name__ == "__main__":
    main()
