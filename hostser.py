from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 4096
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def accept_connection():
	while True:
		client, client_address = SERVER.accept()
		print("%s:%s has connected" % client_address)
		client.send(bytes('You have connected succesfuly, type name and enter'))
		addresses[client] = client_address
		Thread(target=handle_client, args=(client)).start()
def handle_client(client):
	name = client.recv(BUFSIZ).decode(utf8)
	welcome = 'hello %s to close the program type {quit} ' % name
	client.send(bytes(welcome, 'utf8'))
	msg = "%s has joined the chat!" % name
	broadcast(bytes(msg, "utf8"))
	clients[client] = name
	while True:
		msg = client.recv(BUFSIZ)
		if msg != (bytes("{quit}", "utf8")):
			broadcast(msg, name+": ")
		else:
			client.send(bytes("{quit}", "utf8"))
			client.close()
			del clients[client]
			broadcast(bytes("%s has left" % name, "utf8"))
			break


		'''
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
            '''
def broadcast(msg, prefix=''):
	for sock in clients:
		sock.send(bytes(prefix, 'utf8')+msg)
	if __name__ == '__main__':
		SERVER.listen(5)
		ACCEPT_THREAD = Thread(target=accept_incoming_connections)
		ACCEPT_THREAD.start()  # Starts the infinite loop.
		ACCEPT_THREAD.join()
		SERVER.close()
    	



    	


