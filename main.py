from socket import *

serverPort = 9977
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)

    # Check the request path
    if sentence.startswith("GET /ar "):
        # Send the main_ar.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())

        with open("main_Ar.html", "rb") as f:

            connectionSocket.send(f.read())

    elif sentence.startswith("GET / ") or sentence.startswith("GET /en "):
        # Send the main_en.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("main_En.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /css/style.css "):
        # Send the style.css file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/css \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("css/style.css", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /background1.jpg"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("background1.jpg", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /background1.png"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("background1.png", "rb") as f:
            connectionSocket.send(f.read())        

    elif sentence.startswith("GET /salwa.png"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("salwa.png", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /sondos.png"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("sondos.png", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /masa.png"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("masa.png", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /salwa.jpg"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("salwa.jpg", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /sondos.jpg"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("sondos.jpg", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /masa.jpg"):
        # Send the bzu.png file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("masa.jpg", "rb") as f:
            connectionSocket.send(f.read())        

    elif sentence.startswith("GET /yt "):
        # Redirect to Google
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://youtube.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif sentence.startswith("GET /so "):
        # Redirect to Stack Overflow
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(
            "Location: https://stackoverflow.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif sentence.startswith("GET /rt "):
        # Redirect to Birzeit University
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(
            "Location: https://ritaj.birzeit.edu/register/ \r\n".encode())

    else:
        # Send a 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("error.html", "rb") as f:
            connectionSocket.send(f.read())

    # Close the connection
    connectionSocket.close()