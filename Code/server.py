import socket
import threading
import random
import weakref
import time
from threading import *
print_lock = threading.Lock()
Players = {}
players_database = {
}
total_players = 0
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
servername = str(input("What's Your classroom name?"))
    
port = random.randint(10000,65535)
print (host)
print (port)
serversocket.bind((host, port))
##SERVER STARTEDDD++++++++++============
class Player(Thread):
    instances = []
    def __init__(self, name, points,socket, address):
        Thread.__init__(self)
        self.__class__.instances.append(weakref.proxy(self))
        self.id = 1
        self.name = name
        self.points = points
        self.sock = socket
        self.addr = address
        self.start()
    def renameplayer(self,name):
        players_database.pop(self.name, None)
        players_database[name] = [f"{name}",0,self.sock, self.addr]
        self.name = name
    def run(self):
        while 1:
            print(f"Recieved {self.name}")
            try:
                datafromplayer = self.sock.recv(1024).decode()
                self.renameplayer(datafromplayer)
                nameinb = b = self.name.encode('utf-8')
                servernameinb = b = servername.encode('utf-8')
                self.sock.send(b'Hello ' + nameinb + b' Your connection has been reconised. You have joined:' + servernameinb)
            except ConnectionResetError:
                print(f'{self.name} has disconnected removing him now')
                self.delete()
                return
    def addpoint(self,amount):
        self.points += amount
    def removepoints(self, amount):
        self.points += amount
    def getlistofplayers(self):
        for instance in Player.instances:
            print(instance.name)

    def readpoints(self):
        return self.points
    def readname(self):
        return self.name
    def delete(self):
        self.renameplayer("deleted")
        self.name = "deleted"
    
def SetPlayersIn():
    global Players
    for id, data in players_database.items():
        Players[id] = Player(data[0], data[1], data[2], data[3])

def AddPlayer(playername,points,clientsocket, address):
    players_database[playername] = [f"{playername}",0,clientsocket, address]
    SetPlayersIn()
def CheckForPlayers(randomnum):
    #I know you need to setup a listener for clients so yuh
    return
    
def GameStart():
    return
def WaitingLobby(isgamestarting=False):
    if isgamestarting == True:
        GameStart()
    else:
        while isgamestarting == False:
            print("==========Game Lobby=============")
            print("---- Players")
            for item in players_database:
                if item != "deleted" or item != "New":
                    print(f"- {item}")
            time.sleep(5)
serversocket.listen(5)
print ('server started and listening')
waiting = threading.Thread(target=WaitingLobby)
waiting.start()
while 1:
    clientsocket, address = serversocket.accept()
    AddPlayer("New",0,clientsocket, address)