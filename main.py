#Import all functions
import socket
import sys
import argparse
import threading
import time
import timeouts
from datetime import datetime

#Initialize all global variables
global args 
global my_node_no
global connected_peers
global my_key
global debug_mode 
debug_mode = True
global exited
exited = False

base_port = 50000
UDP_IP = "127.0.0.1"


#Start all functions
def send():
   
   global exited
   time.sleep(2)
   
   key = str(input("Enter key to check value:"))
   
   if key == "exit":
      exited = True
   UDP_PORT = base_port+int(my_node_no)
   #key = str(5)
   MESSAGE = "R;;"+str(my_node_no)+";;"+str(datetime.now().time())+";;"+key+";;value;;"


   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
   
   for nodes in connected_peers:
      MESSAGE_SEND = (MESSAGE+str(nodes))
      sock.sendto(bytes(MESSAGE_SEND,"UTF-8"), (UDP_IP, UDP_PORT))


def recieve():

   UDP_PORT = base_port+int(my_node_no)

   serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   serverSock.bind((UDP_IP, UDP_PORT))

   print("Started listener")
   while True:
   
       if exited == True:
          break
       data, addr = serverSock.recvfrom(1024)

       print("Recieved data: {0}".format(data.decode('utf-8')))
       message1 = data.decode('utf-8')
       message = message1.split(";;")
       if int(message[1]) == int(my_node_no):
           print("Got my node")
           if message[4] == "value":
           	print("Message not recieved")
           else:
           	print("Response is: {0}\n Path traversed is:\n{1}".format(message[4],message[5]))
           	
       else:
           send_message = message1+" -> "+str(my_node_no)
           sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
           for nodes in connected_peers:
      		MESSAGE_SEND = (MESSAGE+str(nodes))
     		sock.sendto(bytes(MESSAGE_SEND,"UTF-8"), (UDP_IP, UDP_PORT))


def init():
   global args
   global my_node_no
   global connected_peers
   global my_key
   global debug_mode 

   parser = argparse.ArgumentParser(description="A program for implementing DHT")
   parser.add_argument('-i',help="Current node number", type=int)
   parser.add_argument('-n',help="List of peers near you", required=True)
   parser.add_argument('-s',help="Key value held by node", type=int, required=True)
   parser.add_argument('-m',help="Number of bits")
   parser.add_argument('-a',help="Send DHT key to all connected nodes")
   parser.add_argument('-d',help="Enable debug mode")
   args = vars(parser.parse_args())

   my_node_no = args['i']
   connected_peers1 = str(args['n'])
   connected_peers = connected_peers1.split(",")
   my_key = args['s']
   

   print("All values initiated")
   print("Current node:{0}".format(args['i']))
   print("Connected node:{0}".format(args['n']))
   print("Key value:{0}\n\n--------".format(args['s']))


if __name__ == "__main__":
   init()
   threading.Thread( target=recieve ).start()
   threading.Thread( target=send ).start()

   #timeouts.bar(3)
   
