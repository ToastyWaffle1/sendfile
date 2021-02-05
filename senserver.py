import os
import socket
import tqdm
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5001

BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
#print('listening as'+SERVER_HOST+int(SERVER_PORT))
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept()
#print(''+address+'is now connected')
print(f"[+] {address} is connected.")
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = os.path.basename(filename)
filesize = int(filesize)
# tqdm
bar = tqdm.tqdm(range(filesize), "Sending "+filename, unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, 'wb') as f:
	for _ in bar:
		bytes_read = client_socket.recv(BUFFER_SIZE)
		if not bytes_read:
			break
		f.write(bytes_read)
		#s.sendall(bytes_read)
		bar.update(len(bytes_read))
client_socket.close()
s.close()
 
