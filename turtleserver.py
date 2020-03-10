import turtle
import socket

hostname = "localhost"
port = 7000

wn = turtle.Screen()
wn.title("Turtle Server")
wn.setup(width=1024, height=768, startx=20, starty=20)

obj1 = turtle.Turtle()
obj1.shape("turtle")

sock = socket.socket()
sock.bind((hostname, port))
sock.listen()
conn, addr = sock.accept()

colors = ["red", "blue", "green"]
colorIdx = 0

while True:
    cmessage = conn.recv(1024)
    cmd = cmessage.decode()
    if cmd == "quit": break
    elif cmd == "w":
        obj1.forward(12)
    elif cmd == "s":
        obj1.backward(12)
    elif cmd == "a":
        obj1.left(12)
    elif cmd == "d":
        obj1.right(12)
    elif cmd == "left":
        colorIdx = colorIdx - 1
        if colorIdx < 0:
            colorIdx = 2
        obj1.color(colors[colorIdx])
    elif cmd == "right":
        colorIdx = colorIdx + 1
        if colorIdx > 2:
            colorIdx = 0
        obj1.color(colors[colorIdx])
    elif cmd == "up":
        size = obj1.turtlesize()
        increase = tuple([num + 1 for num in size])
        obj1.turtlesize(*increase)
    elif cmd == "down":
        size = obj1.turtlesize()
        decrease = tuple([num - 1 for num in size])
        obj1.turtlesize(*decrease)

sock.close()
wn.bye()