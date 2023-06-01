import socket
import time


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server_address = ('192.168.255.255', 8855)

    while True:
        student_name = "Salwa Fayyad"
        message = f"{student_name},{socket.gethostbyname(socket.gethostname())}"
        client_socket.sendto(message.encode(), server_address)
        print(f"Sent message: {message} at {time.strftime(' %H:%M:%S')}")
        time.sleep(2)


if __name__ == '__main__':
    main()