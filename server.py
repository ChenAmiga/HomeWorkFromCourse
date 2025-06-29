import socket
localHost="127.0.0.1"
port= 65535
def receive(newP, localHost, port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((localHost,port))
    s.listen(1)
    newS, address=s.accept()
    print ("connected to: ", address)
    with open (newP,"wb") as file:
        while True:
            data= newS.recv(1024)
            if not data:
                break
            file.write(data)
    s.close()

receive("newText",localHost, port)