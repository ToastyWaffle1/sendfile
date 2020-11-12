import tqdm 
import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#specify ip addies here
host = input('enter the host ip')

port = input('enter port')
filename = input('enter the name of the file you want to send: ')
filesize = os.path.getsize(filename)
print(filesize)
s = socket.socket()
	
s.connect((host, int(port)))
print('You are connecting to '+host+port)
print('connected')
s.send('filename+SEPARATOR+filesize'.encode())

#tqdm starts here
bar = tqdm.tqdm(range(filesize), "Sending "+filename".", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename 'rb') as f:
	for _ in progress:
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break
		s.sendall(bytes_read)
		progress.update(len(bytes_read))
s.close()
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
