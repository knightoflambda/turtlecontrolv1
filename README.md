# IT011FP - turtlecontrolv1

Controlling Python's turtle using tkinter and network programming

## Author
* **Bea Glennel Lee**

## How to Setup
On a Windows machine, open the command prompt and type **ipconfig /all**.

## Getting Started
The program is a combination of image processing and network programming, using the libraries **turtle**, **tkinter** and **socket**. 

The project is composed of only two files, *turtleserver.py* and *turtleclient.py*. 

*turtleserver.py* is the one responsible for creating the turtle graphics, the screen and the server.

On the other hand, *turtleclient.py* is responsible for creating an empty tkinter window to receive keypresses, and also connecting to the sever using the provided hostname and port.

Upon successfully connecting to *turtleserver*, *turtleclient* waits for keypresses from the user using **tkinter**'s keyevents. It only accepts the keys w, s, a, d, ESC and the arrow keys.

Once it receives the appropriate keys, it translates it into string commands and sends it into the server. When the server receives the string commands, it calls the turtle object and changes the object according to the command set.
