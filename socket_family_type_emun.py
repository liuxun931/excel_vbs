#!/usr/bin/python3

import socket, threading, os, subprocess


'''Here I am going to list all possible socket with each socket.family and socket.type'''
'''Then I will send out traffic and capture traffic to files to check.'''
'''By doing so, I will get to know how to send out each kind of traffic packets.'''t 
'''Output file will come up at same path with this running script.'''


# step 1 list all socket family and types 

def list_family():
    return list(socket.AddressFamily)

def list_type():
    return list(socket.SocketKind)

# step 2 try to set socket for each family and type

sfamily = list_family()
skind = list_type()


def set_sock(fam, typ):
    os.system("echo '' > ./sockets.txt")
    for f in sfamily:
        for k in skind:
            for pto in range(0, 254):
                try:
                    sock = socket.socket(family = f, type = k, proto=pto)
                    print(sock)
                    os.popen("echo 'socket set %s' >> ./sockets.txt" %sock)
                    sock.connect('10.100.100.73', 443)
                    sock.close()
                except Exception as e:
                    print(e)

def main():
    t = threading.Thread(target=set_sock, args=(sfamily, skind))
    t.start()

if __name__ == "__main__":
    main()