import tkinter
import socket

hostname = "localhost"
port = 7000
socket = socket.socket()
socket.connect((hostname, port))
print("Client has connected to server")
root = tkinter.Tk()
frame = tkinter.Frame(root, width=100, height=100)
entry = tkinter.Entry(frame)
entry.grid(row=0)
tkinter.Label(frame, text="Forward: w").grid(row=1)
tkinter.Label(frame, text="Backward: s").grid(row=2)
tkinter.Label(frame, text="Tilt left: a").grid(row=3)
tkinter.Label(frame, text="Tilt right: d").grid(row=4)
tkinter.Label(frame, text="Quit: ESC or q").grid(row=5)
tkinter.Label(frame, text="Size increase: arrow up or i").grid(row=6)
tkinter.Label(frame, text="Size decrease: arrow down or k").grid(row=7)
tkinter.Label(frame, text="Color swap left: arrow left or j").grid(row=8)
tkinter.Label(frame, text="Color swap right: arrow right or l ").grid(row=9)
def key(event):
    ch = event.char
    print("pressed: " + ch)
    if ch == "w":
        socket.send(ch.encode())
    elif ch == "s":
        socket.send(ch.encode())
    elif ch == "a":
        socket.send(ch.encode())
    elif ch == "d":
        socket.send(ch.encode())
    elif ch == "i":
        arrowCommand = "up"
        socket.send(arrowCommand.encode())
    elif ch == "k":
        arrowCommand = "down"
        socket.send(arrowCommand.encode())
    elif ch == "j":
        arrowCommand = "left"
        socket.send(arrowCommand.encode())
    elif ch == "l":
        arrowCommand = "right"
        socket.send(arrowCommand.encode())
    elif ord(ch) == 27 or ch == "q":
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

entry.bind("<Key>", key)
entry.bind("<Left>", left)
entry.bind("<Right>", right)
entry.bind("<Up>", up)
entry.bind("<Down>", down)
frame.pack()
root.mainloop()