**Requirements**

+ Ensure you have python pip `sudo apt-get install python-pip`
+ then install flask `sudo pip install flask`
+ then install request `sudo pip install requests`
**Flask**



Is a web framework which provides tools and libraries to build web
applications. The flask framework is written in python and it is easy to
build web application using simple python scripts.

Interesting read: <http://flask.pocoo.org/>

<https://pythonspot.com/flask-web-app-with-python/>

<https://www.fullstackpython.com/flask.html>

**HTTP**: Hyper Text Transfer Protocol is designed for communication
between client and servers. HTTP methods are very useful in web
applications.

**HTTP methods**: Indicates a desired action to be taken on a resource.

Some useful methods are: GET, POST, PUT, and DELETE

Definition for the HTTP methods can be found at
<http://flask.pocoo.org/docs/0.12/quickstart/>

**server.py**

The simple receiver script shows use of POST and GET HTTP methods. Here
a client posts a message to the receiver. Also once it receives the get
request, it puts the data to the browser.

The data can be seen on the browser at
"http://localhost:4000/read\_request/10"

![recv.png](https://github.com/vu-resilient-distributed-18/vu-resilient-distributed-18.github.io/blob/master/examples/Flask/recv.png)

**client.py**

This is used to post requests to the receiver. It sends a json message.
It can also get the content from the url and print the response. This is
a simple script which is used to print the responses. After execution
you can see both the response messages being printed on your terminal.

![send.png](https://github.com/vu-resilient-distributed-18/vu-resilient-distributed-18.github.io/blob/master/examples/Flask/send.png)

How to run:

Open a terminal and run the server.py. Then on another terminal run
the client.py.

Now open your browser and type in
<http://localhost:4000/read_request/10> to view the data.

You can see a message being displayed on your browser.
