from socket import *
import tkinter
import os
from threading import *
#s = socket.socket()
def receive():
	while True:
		try:
			msg = client_socket.recv(BUFSIZ).decode('utf8')
			msg_list.insert(tkinter.END, msg)
		except OSError:
			break
def send(event=None):
	msg = my_msg.get()
	my_msg.set('')
	client_socket.send(bytes(msg, 'utf8'))
	if msg == "{quit}":
		client.socket.close()
		top.quit()
def fileupload():
	os.system('python sen.py')
def receivefile():
	os.system('python senserver.py')

#def UploadAction(event=None):
 #   filename = filedialog.askopenfilename()
  #  print('Selected:', filename)

#root = tkinter.Tk()
#button = tkinter.Button(root, text='Open', command=UploadAction)
#button.pack()
'''
def sendfile(event=None):
	filename = input('enter the name of the file you want to send: ')
	filesize = os.path.getsize(filename)
	print(filesize)
	s.send(f"{filename}{SEPARATOR}{filesize}".encode())

		
def send_file(event=None):
	msg = my_msg.get()
	my_msg.set('')
	client_socket.send(bytes(msg, 'utf8'))
	if msg == "{quit}":
		client.socket.close()
		top.quit()
		'''
def on_closing(event=None):
	my_msg.set = "{quit}"
	send()
top = tkinter.Tk()
top.title('Chatter')

message_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set('type message')
scrollbar = tkinter.Scrollbar(message_frame)


msg_list = tkinter.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
message_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
file_button = tkinter.Button(top, text="Send File", command=fileupload)
file_button.pack()
receive_button = tkinter.Button(top, text="receive file", command=receivefile)
receive_button.pack()
#root = tkinter.Tk()
#button = tkinter.Button(root, text='Open', command=UploadAction)
#button.pack()
#file_button = tkinter.Button(top, text="file", command=sendfile)
#file_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('enter the HOST ip')

PORT = input('enter PORT')
if not PORT:
	PORT = 5001
else: 
	PORT = int(PORT)
BUFSIZ = 4096
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.

tkinter.mainloop()
