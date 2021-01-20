import tkinter as tk
#import ChatClient
from tkinter import *
import os
def quit():
    exit()
def connectbutton():
    with open('sen.py') as infile:
        exec(infile.read())

m1 = PanedWindow()
m1.pack(fill = BOTH, expand=1)

left = Entry(m1, bd = 5)
m1.add(left)
m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)

top = Scale(m2, orient = VERTICAL)
m2.add(top)
top = Button(m2, text= 'quit', command = quit)
m2.add(top)
bottom = Button(m2, text= 'ok', command = connectbutton)
m2.add(bottom)
mainloop()