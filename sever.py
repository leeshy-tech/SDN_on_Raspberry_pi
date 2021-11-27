# coding=gbk
# a simple socket communication project,running on the common node
import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(("10.0.0.4",1234))        # bind a IP and port to this socket
    s.listen()
    c,addr = s.accept()
    with c:
        print(addr,"connected.")

        while True:
            data = c.recv(1024)
            if not data:
                break
            print("Received",repr(data))  # print RXD