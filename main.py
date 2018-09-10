#Import all functions
import socket
import sys
import argparse
import threading
import time
import multiprocessing
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
global sent_datas
sent_datas = " "
global now_sent 
now_sent= False
global wait_to_recieve
wait_to_recieve = False
global already_parsed
already_parsed = set()

global p

base_port = 50000
UDP_IP = "127.0.0.1"
timeout_node = 10


#Start all functions
def send():
	
	global exited
	global now_sent
	global already_parsed
	global p
	global wait_to_recieve
	global sent_datas

	while True:
		time.sleep(1)
		#print(end)
		
		key = str(input("\n\n------\nEnter key to check value:"))
		
		if key == "exit":
			exited = True
		UDP_PORT = base_port+int(my_node_no)

		#Message format -> R ;; from ;; time_sent ;; requsted_key ;; key value ;; nodes traversed

		current_time=str(time.time())
		MESSAGE = "R;;"+str(my_node_no)+";;"+current_time+";;"+key+";; value ;;"
		sent_datas=str(my_node_no)+current_time


		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
		
		for nodes in connected_peers:
			MESSAGE_SEND2 = (MESSAGE+""+str(my_node_no)+" -> ")
			send_port = base_port+int(nodes)

			if int(nodes) > int(my_node_no):
				print("Message sent to {0}".format(send_port))
				sock.sendto(bytes(MESSAGE_SEND2,"UTF-8"), (UDP_IP, send_port))
				break
				

		time.sleep(5)
		if sent_datas != " ":
			print("No message recieved")
			already_parsed.add(sent_datas)
					



def recieve():

	
	global sent_datas
	global already_parsed

	UDP_PORT = base_port+int(my_node_no)

	serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serverSock.bind((UDP_IP, UDP_PORT))

	print("Started listener\n")
	while True:
		if exited == True:
			break
		


		#Recieve and decode message
		data, addr = serverSock.recvfrom(1024)
		#print("Recieved data: {0}".format(data.decode('utf-8')))
		message1 = data.decode('utf-8')
		message = message1.split(";;")
		
		timed_out = time.time() - float(message[2])

		rec = str(message[1])+str(message[2])

		
		if rec not in already_parsed and timed_out<10:

			if int(message[1]) == int(my_node_no):
				if "Response" not in message1:
					print("Message not recieved")
				else:
					print("\n\n----\n\nGot my node :\n{0}\n".format(message))
					print("Path traversed is:\n{0}".format(message[5]))

					already_parsed.add(rec)
				sent_datas=" "

			elif int(message[3]) == my_key:

					message1 = message1+" -> "+str(message[1])
		
					message1.replace('value',str(my_key*my_key))
					message1.replace("R",str(my_node_no))
					send_message = message1+"\nResponse : " +str(my_key*my_key)
					sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					send_port = base_port+int(message[1])
					sock.sendto(bytes(send_message,"UTF-8"), (UDP_IP, send_port))
					already_parsed.add(rec)


			else:
				message1 = message1+str(my_node_no)+" -> "
		
				#Prepare message sending
				
				send_message = message1
				
				set_add = rec

				already_parsed.add(set_add)

				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
				for nodes in connected_peers:
					if int(nodes) != int(message[1]):
						if int(nodes) > int(my_node_no):
							MESSAGE_SEND = (message1+str(nodes))
							send_port = base_port+int(nodes)
							sock.sendto(bytes(MESSAGE_SEND,"UTF-8"), (UDP_IP, send_port))
							break

def bar():
	for i in range(3):
		time.sleep(1)

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
	
