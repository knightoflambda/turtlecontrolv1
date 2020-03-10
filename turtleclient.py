import tkinter
import socket

hostname = "localhost"
port = 7000
""" 
w = 119
s = 115
a = 97
d = 100
ESC = 27
UP
DOWN
LEFT
RIGHT
"""
socket = socket.socket()
socket.connect((hostname, port))
#if successful conn
root = tkinter.Tk()
frame = tkinter.Frame(root, width=100, height=100)
def key(event):
    ch = event.char
    if ch == "w":
        socket.send(ch.encode())
    elif ch == "s":
        socket.send(ch.encode())
    elif ch == "a":
        socket.send(ch.encode())
    elif ch == "d":
        socket.send(ch.encode())
    elif ord(ch) == 27:
        killCommand = "quit"
        socket.send(killCommand.encode())
        socket.close()
        root.destroy()
def left(event):
    message = "left"
    socket.send(message.encode())
def right(event):
    message = "right"
    socket.send(message.encode())
def up(event):
    message = "up"
    socket.send(message.encode())
def down(event):
    message = "down"
    socket.send(message.encode())

frame.bind("<Key>", key)
frame.bind("<Left>", left)
frame.bind("<Right>", right)
frame.bind("<Up>", up)
frame.bind("<Down>", down)
frame.focus_set()
frame.pack()
root.mainloop()