#Import all functions
import socket
import sys
import getopt
import argparse
import threading
import time


#Initialize all global variables
global args 
global my_node_no
global connected_peers
global my_key

base_port = 50000
UDP_IP = "127.0.0.1"


#Start all functions
def send():
   time.sleep(5)
   UDP_PORT = base_port+int(my_node_no)
   MESSAGE = "Hello, World!"


   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
   sock.sendto(bytes(MESSAGE,"UTF-8"), (UDP_IP, UDP_PORT))


def recieve():

   UDP_PORT = base_port+int(my_node_no)

   serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   serverSock.bind((UDP_IP, UDP_PORT))

   print("Started listener")
   while True:
       data, addr = serverSock.recvfrom(1024)
       print("Recieved data: {0}".format(data.decode('utf-8')))


def init():
   global args
   global my_node_no
   global connected_peers
   global my_key

   parser = argparse.ArgumentParser(description="A program for implementing DHT")
   parser.add_argument('-i',help="Current node number", type=int)
   parser.add_argument('-n',help="List of peers near you", required=True)
   parser.add_argument('-s',help="Key value held by node", type=int, required=True)
   parser.add_argument('-m',help="Number of bits")
   args = vars(parser.parse_args())

   my_node_no = args['i']
   connected_peers = args['n']
   my_key = args['s']

   print("All values initiated")
   print("Current node:{0}".format(args['i']))
   print("Connected node:{0}".format(args['n']))
   print("Key value:{0}\n\n--------".format(args['s']))


if __name__ == "__main__":
   init()
   threading.Thread( target=recieve ).start()
   threading.Thread( target=send ).start()
   