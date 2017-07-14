#coding:utf-8
import socket 
import time
import threading

def TCP(sock,addr):
	print("Accept new connection from %s:%s." %addr)
	while True:
		#接收客户端发送来得数据，接受最大窗口为1024
		recv_data = sock.recv(1024)
		time.sleep(1)
		
		#如果一秒后没有接收到数据，或者接收到"quit",则退出
		if not recv_data or recv_data.decode()=='quit':
			break;
		
		print("Nancsyse-客户端： {0}".format(recv_data.decode('utf-8')),end="\n\n")
		data = input("Nancyse-服务端： ")
		print()
		#发送数据
		#将接收到数据按照utf-8编码规则解码，并且转换成大写，然后发送
		#sock.send(data.decode('utf-8').upper().encode())
		sock.send(data.encode())
		
	#关闭套接字
	sock.close()
	print("Connection from {0}: {0} closed.".format(addr))
	

#创建socket，其中AF_INET:IPv4,AF_INET6:IPv4, SOCK_STREAM:面向流的TCP协议
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定socket,绑定本机的端口10021
server.bind(('127.0.0.1',10021))

#监听socket,等待连接的最大数目为1
server.listen(1)

print("服务器名称：Nancyse-服务器")
print("服务器IP：127.0.0.1")
print("学号：2013011023")
print("姓名：林鹏珊",end="\n\n")
print("*************通信窗口**************")
print("Server is running...")

while True:
	#接受连接请求
	sock,addr=server.accept()
	TCP(sock,addr)

	













