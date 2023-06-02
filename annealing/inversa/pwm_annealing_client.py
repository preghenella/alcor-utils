#! /usr/bin/env python3

import socket
import sys

SOCK='/tmp/arduino_pwm_control.socket'

if len(sys.argv) < 2:
    print('usage: ./client.py [command]')
    sys.exit(0)

command = sys.argv[1]
print(' --- sending command:', command)

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(SOCK)
    s.sendall(command.encode())
