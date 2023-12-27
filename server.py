import socket
import threading
HOST = '127.0.0.1'
PORT = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(socket.gethostbyname(socket.gethostname()))
server.bind((HOST,PORT))
server.listen(100)
clients = []
nicks = []
def broadcast(message):
    for client in clients:
        client.send(message)
def chatwusr(message , nick):
    for i in range(0,len(nicks)):
        if nick == nicks[i]:
            usr = clients[i]
        else:
            print("user not currently in server , try later")
            break
    usr.send(message.encode('ascii'))
def handle(client):
    while True:
        try:
            
            message = client.recv(1024)
            words = message.split()
            for word in words:
                print(word)
            if words[1] == 'dm':
                chatwusr(message , words[2])
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nick = nicks[index]
            broadcast(f"{nick} left the chat".encode('ascii'))
            nicks.remove(index)
            break

def receive():
    while True:
        client , address = server.accept()
        print(f"connected with {str(address)}")
        client.send('Nick'.encode('ascii'))
        nick = client.recv(1024).decode('ascii')
        nicks.append(nick)
        clients.append(client)
        print(f"{nick} is the name of  {client}")
        broadcast(f'{nick}  joined the chat'.encode('ascii'))
        client.send("connect to the server".encode('ascii'))

        thread = threading.Thread(target = handle , args = (client,))
        thread.start()

receive()
