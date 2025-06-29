import socket
localHost="127.0.0.1"
port= 65535
def send(filePath, localHost, port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((localHost,port))
    with open (filePath,"rb") as file:
        while True:
            data=file.read(1024)
            if not data:
                break
            s.send(data)
    s.close()

send(r"C:\Users\alona\HomeWorkFromCourse\textToSend", localHost, port)
