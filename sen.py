import tqdm 
import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#specify ip addies here
host = input('enter the host ip')

port = input('enter port')
filename = input('enter the name of the file you want to send: ')
filesize = os.path.getsize(filename)
print(filesize)
s = socket.socket
	
s.connect((host, port))
print('You are connecting to '+host+port)
print('connected')
s.send('filename+SEPARATOR+filesize'.encode())

#create the socket
'''
try:
	s = socket.socket'
	
	s.connect((host, port))
	print('You are connecting to '+host,port)
	print('connected')
except socket.error as err:
	#if it doesnt create then print this
	print("failed to create socket")
	print("reason %s" %str(err))
	##sys.exit()
'''