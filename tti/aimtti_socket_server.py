#! /usr/bin/env python3

import socket
import argparse
import os

### arguments
parser = argparse.ArgumentParser(description='a server', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--address', type=str, default='10.0.8.21', help='IP address')
parser.add_argument('--port', type=int, default=9221, help='port')
args = parser.parse_args()

### instrument communication socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.address, args.port)

def connect():
    sock.connect(server_address)

def close():
    sock.close()

def send(command):
    command += '\n'
    sock.send(command.encode())

def recv():
    data = sock.recv(4096)
    data = data.decode()
    while data[-1] != '\n':
        data += sock.recv(4096)
    return data.strip()

def ask(cmd):
    send(cmd)
    return recv()

connect()

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.bind(SOCK)
    s.listen()
    
    try:
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode()
                    print('--- received command:', command)
                    if command[-1:] == '?':
                        print('--- ask instrument:', command)
                        data = ask(command)
                        print('--- sending data:', data)
                        conn.sendall(data.encode())
                    else:
                        print(' --- send instrument:', command)
                        send(command)
    except Exception as e:
      print(e)
      pass
    
close()
