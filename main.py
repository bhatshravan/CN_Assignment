import socket
import sys

#sys.argv[1]

UDP_IP = "127.0.0.1"
UDP_PORT = 6789
MESSAGE = "Hello, World!"

print("UDP target IP:{0}".format(UDP_IP))
print("UDP target port:{0}".format(UDP_PORT))
print("message:{0}".format(MESSAGE))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE,"UTF-8"), (UDP_IP, UDP_PORT))