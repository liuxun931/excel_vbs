import os, threading, json
import socket as sock

'''
play with socket to send udp packet, or any packets;
first to test udp broadcase packets.
'''

port = 8888
interface = '192.168.10.107'
mcast = '224.0.1.0'
mgroup = (mcast, port)
data = json.dumps({"sendername": "liux", "context": "sexy-broadcasting"}).encode('utf-8')

ss = sock.socket(family=sock.AddressFamily.AF_INET, type=sock.SocketKind.SOCK_DGRAM, proto=sock.IPPROTO_UDP)

ss.setsockopt(sock.SOL_SOCKET, sock.SO_BROADCAST, 1)

ss.setsockopt(sock.IPPROTO_IP, sock.IP_MULTICAST_TTL, 128)


ss.setsockopt(sock.IPPROTO_IP, sock.IP_MULTICAST_IF, sock.inet_aton(interface))
print("print mcast address: %s" %ss.getsockopt(sock.IPPROTO_IP, sock.IP_MULTICAST_IF))

ss.sendto(data, (mcast, port))
