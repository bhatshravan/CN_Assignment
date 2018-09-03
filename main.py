#Import all functions
import socket
import sys
import getopt
import argparse
import signal


#Initialize all global variables
global args 
global my_node_no
global connected_peers
global my_key

#Start all functions
def send():
   UDP_IP = "127.0.0.1"
   UDP_PORT = 6789
   MESSAGE = "Hello, World!"

   print("UDP target IP:{0}".format(UDP_IP))
   print("UDP target port:{0}".format(UDP_PORT))
   print("message:{0}".format(MESSAGE))

   print("Cuurent node:{0}".format(args['i']))
   print("Connected node:{0}".format(args['n']))
   print("Key value:{0}".format(args['s']))

   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
   sock.sendto(bytes(MESSAGE,"UTF-8"), (UDP_IP, UDP_PORT))


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


if __name__ == "__main__":
   init()
   send()