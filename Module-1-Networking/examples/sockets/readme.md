# Overview

Sockets are the primary network communication mechanism in operating systems. 

## Examples

The typical network protocol used with sockets is either TCP or UDP. In most cases the receiving socket blocks unless the message arrive. Take a look at the following examples.

* Python TCP example [https://pymotw.com/3/socket/tcp.html](https://pymotw.com/3/socket/tcp.html)
* python UDP example [https://pymotw.com/3/socket/udp.html](https://pymotw.com/3/socket/udp.html)

### Non Blocking

However, sometime we might not want to block for sockets. If a process is only waiting on a single socket it can use the non blocking option for the socket and rely on external coordination to decide when to read the message or not.
In Python, you use `socket.setblocking(0)` to make it non-blocking. In C, it’s more complex, you use `O_NONBLOCK`. You do this after creating the socket, but before using it. Take a look at [https://pymotw.com/3/socket/nonblocking.html](https://pymotw.com/3/socket/nonblocking.html)

### Select and Poll

In case we are are dealing with more than one sockets or want the system to tell us when the socket is ready we can use the select and poll mechanisms. Look at [https://pymotw.com/3/select/](https://pymotw.com/3/select/)
