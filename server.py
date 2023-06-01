import socket
import time


def main():
    server_address = ('', 8855)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)

    clients = {}
    count = 0

    print("Server is listening on port 8855...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        client_name, client_ip = message.split(",")
        clients[client_ip] = client_name

        count += 1
        print(f"Received message from {client_name} at {time.strftime(' %H:%M:%S')}")

        print("=== Recent Messages ===")
        for ip, name in clients.items():
                print(f"Received message from {name} at {time.strftime(' %H:%M:%S')}")

        clients = {}
if __name__ == '__main__':
    main()