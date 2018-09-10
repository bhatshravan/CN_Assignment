Github repo for Computer Network assignment 1.

## Info

### Members:
* Shravan Bhat - 1KS16CS092
* Shashank Kavur - 1KS16CS090
* Aravind K.L. - 1KS14CS019

### Problem statement:
Consider implementing a DHT with shortcuts having N peers. Each peer is provided with information about the peer knows. The implementation of keys is done using immediate successor. Each peer will run as a separate program. Each peer will ask for an input of key value for which it needs to obtain a response. The response should given as square of the key value.

### Synopsis:
This is a program to implement dhT using the concept of successive nodes in file main.py and send to all connected nodes in all.py.

## Installation
* Install Python 3.7.0 and add it to PATH


## Usage
* Main.py for successive node implementation
* All.py for sending to all connected nodes. This is slower for yields better results.

python main.py -i <my_node> -n <connected_node_1, connected_node_2> -s <key_value>
or else type python -h for help


## Working
* First the program takes input of all values and gets ready
* Then it makes 2 threads- Thread 1 for searching a key with user input, Thread 2 for transmitting any udp messages
* If user enters input, then the send() function will broadcast message to succesive only 1 node in main.py and to all nodes in all.py. If there is message recieved in 5 seconds then it is accepted or else it assumes that the key is lost/not available.
* Recieve function continuously listens for UDP messages. Once recieved, it does 1 of the 3-
1. It checks if message from itself, if true than it extracts the response value and displays it or else it assumes that it was a re-broadcast by a connected node and discards it
2. If it is not from itself, then it transmits packet to next successive node.
3. If it has the key requested, than it responds to original node with response value which is the square of the number.

## Challanges faced
* Understanding the problem
* Decipering and creating broadcast messages format
* Adding timeouts 
* Implementing the broadcast mechanism for successive nodes

## Sample run

### Input

Terminal 1: python main.py -i 1 -n 5,6 -s 10
Terminal 2: python main.py -i 5 -n 9,31 -s 20
Terminal 3: python main.py -i 6 -n 5,9 -s 30
Terminal 4: python main.py -i 9 -n 1,32 -s 40


After all nodes are initialized, using terminal 1-

Output:

All values initiated
Current node:1
Connected node:5,6
Key value:10

--------
Started listener



------
Enter key to check value:40
Message sent to 50005


----

Got my node :
['R', '1', '1536584337.5082974', '40', ' value ', '1 -> 5 -> 99 -> \nResponse : 1600']

Path traversed is:
1 -> 5 -> 9 -> 
Response : 1600


------
Enter key to check value:90
Message sent to 50005
No message recieved



