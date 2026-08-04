# 步骤1：导入模块、创建socket对象
import socket
socket_client = socket.socket()

# 步骤2：连接指定服务端（传入元组：IP地址,端口号）
socket_client.connect(("localhost", 8888))

# 步骤3：循环发送消息
while True:
    # 控制台输入待发送消息
    send_msg = input("请输入要发送的消息：")
    # 约定exit作为退出标识，结束循环
    if send_msg == 'exit':
        break
    # 字符串用UTF-8编码为字节数组后发送
    socket_client.send(send_msg.encode("UTF-8"))

# 4. 接收服务端返回消息
while True:
    # 输入消息并直接编码为字节类型发送
    send_msg = input("请输入要发送的消息").encode("UTF-8")
    socket_client.send(send_msg)

    # recv(1024)：1024为缓冲区大小，阻塞式等待服务端数据
    recv_data = socket_client.recv(1024)
    # 将字节数据用UTF-8解码为字符串打印
    print("服务端回复消息为：", recv_data.decode("UTF-8"))

# 5. 关闭连接
socket_client.close()  # 通信结束释放资源

# 通信结束关闭客户端连接
socket_client.close()