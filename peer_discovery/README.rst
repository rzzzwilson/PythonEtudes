The code here is an exploration into discovering other clients on the local
network.  This can be useful in games and the like, where we need to get the
IP of a peer without using a central broker server.

The idea is to use UDP broadcast messages.  Each client will::

    until a peer is found:
        broadcast one UDP message
        listen for broadcast messages
    send an ACK message to the other peer

Once an ACK message is received each copy of the code will return the IP of
the peer.

Executing::

    python3 test.py

will run the test code.  Run another instance on the same machine or another
machine on the same subnet.
