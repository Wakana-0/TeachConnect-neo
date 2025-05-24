import socket
from loguru import logger

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(message ,ip = '127.0.0.1',port = 11223):
    try:
        sock.connect((ip, port))
        logger.debug(f"连接到 {ip}:{port}")
        sock.sendall(message.encode())
        logger.debug(f"发送消息: {message}")
        sock.close()
        logger.debug(f"关闭连接")
    except Exception as e:
        logger.error(f"Error while sending message: {e}")
        return False
    return True
