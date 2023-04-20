#_*_coding:utf-8_*_

import socket, os 



def get_sockbuff(sock):
	recv_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
	send_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
	print("receive_buf_size: %s, \n send_buf_size: %s" %(recv_buff, send_buff))



def set_sockbuff(sock, rcvbuf, sndbuf):
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, rcvbuf)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, sndbuf)
	print("set receive_buf_size: %s, \n set send_buf_size: %s" %(rcvbuf, sndbuf))



def main():
	sock = socket.socket()
	get_sockbuff(sock)
	print("change buff...")
	set_sockbuff(sock, 4096, 2048)
	get_sockbuff(sock)

if __name__ == "__main__":
	main()
