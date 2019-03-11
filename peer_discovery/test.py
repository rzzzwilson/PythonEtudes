"""
Module that finds a peer on the local network.

    port = 50000
    peer_ip = get_peer(port, timeout=0.5)
"""

import time
import socket

# different types of messages
PeerPing = bytes('PeerPing', 'utf-8')
PeerAck = bytes('PeerAck', 'utf-8')

def send_ack(ip, port):
    """Send a UDP ACK message.

    ip       the IP to send ACK message to
    port     the port number to send on

    Creates socket connection, sends one ACK message then closes socket.
    """

    # create socket to peer, send message, close socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(PeerAck, (ip, port))
    sock.close()

def send_udp_broadcast(port, timeout=0.1):
    """Send a UDP broadcast message.

    id_msg   the message identifying the peer "group"
    port     the port number to send on
    timeout  the send timeout

    Sends one message then closes socket.
    """

    # create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.settimeout(timeout)

    # send a 'ping' message
    server.sendto(PeerPing, ('<broadcast>', port))

    # close socket
    server.close()

def recv_udp(port, timeout=0.1):
    """Listen on the given port for a UDP message.

    port    the port top listen on

    Return the IP of the sender if a peer message was received, else return None.
    """

    # create listening socket for UDP messages
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.settimeout(timeout)
    try:
        client.bind(('', port))
    except OSError:
        return None

    # listen for any UDP broadcast messages
    try:
        m = client.recvfrom(1024)
    except socket.timeout:
        return None

    # close socket
    client.close()

    # check msg type
    if m[0] in (PeerPing, PeerAck):
        return m[1][0]

    return None

def get_peer(port, timeout=0.5):
    """Find a peer on the local network.

    port     the port number to look on
    timeout  the timeout 

    Returns the IP address of the first peer found.
    Returns None if not found inside timeout period.
    """

    # alternate between sending and then receiving UDP messages
    # until we get a peer IP
    peer_ip = None
    while peer_ip is None:
        send_udp_broadcast(port, timeout)
        peer_ip = recv_udp(port, timeout)

    # got peer IP, send messages back saying we are a pair
    time.sleep(timeout / 2)     # need a pause for some reason
    send_ack(peer_ip, port)

    return peer_ip


if __name__ == '__main__':
    port = 50000

    peer = get_peer(port)
    print(f'peer={peer}')
