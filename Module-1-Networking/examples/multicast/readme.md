# Overview

Multicast is a networking construct where a sender can send a message to more than one receiver within the network. Note that this is different than broadcast where the sender message is received by all receivers in the network listening on the port on which the message was sent. Multicast is a very useful construct when you want to inform a large number of processes about some activity. As you can guess multicast requires the support of switch and network interfaces which have to selectiviely forward the message as required.

# Examples

* mcast.py - This example shows how to create multicast receivers and senders. Multicast is a selective group communication mechanism. Broadcast is the way to send message to everyone in a local network. 
* Other multicast example [https://pymotw.com/3/socket/multicast.html](https://pymotw.com/3/socket/multicast.html)

# Running

```
python2 mcast.py listen
```

and 

```
python2 mcast.py announce
```

