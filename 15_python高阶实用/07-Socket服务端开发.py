# Socket
# socket (简称:套接字) 是进程之间通信一个工具，好比现实生活中的插座，所有的家用电器要想工作都是基于插座进行，
# 进程之间想要进行网络通信需要socket。
# Socket负责进程之间的网络数据传输，好比数据的搬运工。
#
# 原理示意图：
# 进程1 <--socket--> 传输数据 <--socket--> 进程2
#
# 大多数软件（QQ、微信、浏览器等）都使用到了Socket进行网络通讯

# 客户端和服务端
# 2个进程之间通过Socket进行相互通讯，就必须有服务端和客户端

# Socket服务端：等待其它进程的连接、可接受发来的消息、可以回复消息
# Socket客户端：主动连接服务端、可以发送消息、可以接收回复

# 通信模型
# 客户端  --发送-->  服务端
# 客户端  <--回复--  服务端
# 多个客户端可以同时与同一个服务端建立连接通信

# 导入socket包
import socket
from ctypes.wintypes import MSG

# 1. 创建socket对象
socket_server = socket.socket()

# 2. 绑定IP与端口
socket_server.bind(("localhost", 8888))

# 3. 开启监听
socket_server.listen(1)  # listen方法内接受一个整数传参数，表示接受的连接数量

# 4. 等待客户端连接
# result:tuple = socket_server.accept()
# conn = result[0]    # 客户端和服务端的连接对象
# address = result[1]  # 客户端的地址信息
conn,address = socket_server.accept()
# accept()是阻塞的方法，等待客户端的连接，如果没有连接，就卡在这一行不向下执行力
print(f"接收到客户端连接，连接来自：{address}")

while True:
    # 接收客户端消息：要实用客户端和服务端的本次连接对象，而非socket_server的对象
    data:str = conn.recv(1024)
    print("客户端消息：", data.decode("UTF-8"))

    # 回复消息
    msg = input("请输入你要和客户端回复的消息: ").encode("UTF-8")
    if msg == 'exit':
        break
    conn.send(msg.decode("UTF-8"))

# 关闭连接
conn.close()
socket_server.close()