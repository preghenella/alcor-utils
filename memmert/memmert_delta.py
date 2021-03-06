#! /usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall('IN_SP_11'.encode())
    tset = float(s.recv(1024).decode())
    s.sendall('IN_PV_11'.encode())
    tcur = float(s.recv(1024).decode())
    print(tcur - tset)
