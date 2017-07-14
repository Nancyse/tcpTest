#coding:utf-8
#http://www.cnblogs.com/whatbeg/p/5155524.html
import socket

#创建socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
client.connect(("127.0.0.1",10021))

print("客户端：Nancsy-客户端：")
print("客户端IP: 127.0.0.1")
print("学号： 2013011023")
print("姓名： 林鹏珊",end='\n\n')
print("**************通信窗口**************")

while True:
	data=input("Nancyse-客户端: ")
	
	#如果发送的是“quit”
	if data=='quit':
		break
	
	#发送数据
	client.send(data.encode())
	print()
	
	#接受数据并打印出来
	recv_data=client.recv(1024).decode('utf-8')
	print("Nancyse-服务端： {0}".format(recv_data),end="\n\n")
	
client.send(b'quit')

client.close()