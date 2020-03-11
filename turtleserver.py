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
print("Server has received client")
colors = ["red", "blue", "green"]
colorIdx = 0
size = 1
while True:
    cmessage = conn.recv(1024)
    cmd = cmessage.decode()
    print("received: " + cmd)
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
        size = size + 1
        obj1.turtlesize(size, size, size)
    elif cmd == "down":
        size = size - 1
        obj1.turtlesize(size, size, size)

sock.close()
wn.bye()