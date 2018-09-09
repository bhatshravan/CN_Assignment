Github repo for Computer Network assignment 1.


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

## Changelog

### V0.0.7
* Update Readme.md

### V0.0.6
* Addd function timeouts

### V0.0.5
* Optimize the program

### V0.0.4
* Added a proper sending function

### V0.0.3
* Added a client listener

### V0.0.2
* First implementation of socket over UDP in python

### V0.0.1
* Made and initiated README, repo

