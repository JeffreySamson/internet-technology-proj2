import threading
import time
import random
import sys

import socket

"""
User inputs 
    1: lsListenPort
    2: ts1Hostname 
    3: ts1ListenPort 
    4: ts2Hostname 
    5: ts2ListenPort
"""


# Connects to the client
try:
    rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[LS]: Server socket 1 created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
rs.bind(server_binding)
rs.listen(1)
host = socket.gethostname()
print("[LS]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[LS]: Server IP address is {}".format(localhost_ip))
csockid, addr = rs.accept()


# Connects the TS1
try:
    ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[LS]: Client socket for TS1 created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
ts1_port = int(sys.argv[3])
ts1host_addr = socket.gethostbyname(sys.argv[2])

# connect to rs
ts1_binding = (ts1host_addr, ts1_port)
ts1.connect(ts1_binding)


# Connects to TS2
try:
    cls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[LS]: Client socket for TS1 created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# port and hostname from cmd line argument
ts2_port = int(sys.argv[5])
ts2host_addr = socket.gethostbyname(sys.argv[4])

# connect to rs
ts2_binding = (lshost_addr, ls_port)
cls.connect(ls_binding)

while True:
    csockid, addr = rs.accept()
    try:
        while True:
            # Receive data from the server
            data_from_client = csockid.recv(1024)
            message = data_from_client.decode('utf-8')

            ts1.sendall(msg.encode('utf-8'))
            ts2.sendall(msg.encode('utf-8'))
    except:
        pass
