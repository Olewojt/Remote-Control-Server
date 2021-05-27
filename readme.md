# Remote Control
A small project for remote control over other computer using it's console. ***(Windows only)***

## Used libraries

* [socket](https://docs.python.org/3/library/socket.html) - establishing connection
* [subprocess](https://docs.python.org/3/library/subprocess.html) - executing commands
* [threading](https://docs.python.org/3/library/threading.html) - used for sending and receiving at the same time(full duplex or smth)
* [os](https://docs.python.org/3/library/os.html) - exiting purposes
* [time](https://docs.python.org/3/library/time.html)


### How does it work?
Program uses [socket](https://docs.python.org/3/library/socket.html) library to connect to the other computer. Then, after making sure connection is established, it executes commands through console using [subprocess](https://docs.python.org/3/library/subprocess.html). All commands sent to controlled device starts with **"!"**. 

