import socket
import threading
nickname = input("choose a nickname: ")
HOST = '127.0.0.1'
PORT = 6969


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST , PORT))


def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("connection has been closed")
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recive)
recieve_thread.start()
write_thread = threading.Thread(target=write )
write_thread.start()
client.close()

