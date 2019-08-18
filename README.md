# Introduction

The goal of this class is to provide a foundation in the area of realiable distributed computing. This is specially important in order to be able to construct high assurance applications in this era of Internet of Things and Smart Cities. The technical landscape of the technologies in this area is changing rapidly: Memcached (a new kind of key-value store) has displaced standard file system storage, Chubby supports scalable locking and synchronization, ZooKeeper enables consistency-based  distributed services. Big Table manages sparse but enormous data sets. ZeroMQ. MQTT and DDS provide the reliable communication services. 

# Getting Started

In the initial part of this class we will use two linux virtual machines. Follow the instructions at https://github.com/RIAPS/riaps-integration/blob/master/riaps-x86runtime/README.md and load two virtual machines on your computer. When you are importing ensure that you reset the network interface addresses.

Ignore the instructions given in the subsection on "Securing Communication Between the VM and BBBs" because you will not be using beaglebones. 


# Reading Material

 * Textbook: Download from https://link.springer.com/book/10.1007/978-1-4471-2416-0 The book is available for free download from vanderbilt campus.
 * In addition to the textbook we will be assigning several reading materials for the class. 
 
# Class Discussion

 * Class discussion is going to be an important part of this course. I will be assigning papers for class discussion and the discussion will have to be lead by one of the students. 
 

# Syllabus

The course is going to be divided into 5 modules. Each module will end with an assignment and a report on the topic.  

* Module 1: Review of Networking - We will review the concept of sockets, internet
routing, TCP/UDP and DNS. These concepts are the backbone of distributed systems.
* Module 2:  Internet of Things and cloud - We will review internet of things, including the different distributed
application interaction patterns, for example pub/sub, synchronous and asynchronous
point to point communication. You will learn to use or review the use of MQTT,
REST/Websocket and ZeroMQ, DDS in this module. Towards the end of this module
you will build a vehicle-to-vehicle (V2V) communication network between cars in a
simulated environment called TORCS.
* Module 3: Understanding performance bottlenecks, Quality of Service and Failures - In this module we will review what is quality of service, how is it expressed and what
failure means.  It will be important to understand the concept of time synchronization. Additionally, during this module you will get introduced to the FMECA analysis and
will have to analyze the failure modes of the distributed application you have built
during the second module.
* Module 4: Reliability in Distributed systems – In this module you will be introduced
to formal concepts related to reliability in distributed computing systems. We will
discuss various techniques for overcoming failures, and achieving consistency,
availability, and reliability in distributed systems. We will be using the guide to reliable
distributed distributed systems book https://link.springer.com/book/10.1007/978-1-4471-2416-0 for the majority of this module and the next modules to follow.
* Module 5: Reliability techniques and related technologies – In this last module we
discuss several tools and techniques to retrofit reliability to complex systems. We will
review concepts of security schemes, clock synchronization, and transaction schemes
that are used to achieve reliability in practical distributed systems. At the end of this
module you will be able to apply these reliability concepts to the car’s V2V network
assignments.
* Tutorial and experience with [resilient information architecture platform for Smart Grid](https://riaps.isis.vanderbilt.edu) - This will be an invitation based 3 hour tutorial for you. You will be able to see how all the concepts we discussed in the class are implemented in practice. This will be an exciting tutorial and I encourage you to attend it.
* Final Project- the final module for this course is going to be a project, which you will develop
in teams.

