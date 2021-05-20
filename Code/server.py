import socket
import threading
import random
import weakref
import time
from threading import *
import tkinter as tk
from tkinter import ttk
from tkinter import * 
StartServer = True
servername = ""
print_lock = threading.Lock()
Players = {}
players_database = {
}
lobby_gui = ""
endserver = False
total_players = 0
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
LOH = ""

class LobbyGUI:
    def __init__(self, servernamee,LOHH,serverport,master):
        self.master = master
        self.servernamee = servernamee
        self.LOHH = LOHH
        self.serverport = serverport
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Game Lobby', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5, rely=0.1, anchor=CENTER)
        Button(master, text='Start Game', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.StartGame).place(relx=0.1,rely=0.9,anchor=CENTER)
        Button(master, text='Quit', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(relx=0.9,rely=0.9,anchor=CENTER)
        Label(master, text=f"Server Pin: {self.serverport}",bg='#8B8378' ,font=('Helvetica', 20)).place(relx=0.1,rely=0.21,anchor=CENTER)
        Label(master, text=f"Server Name: {self.servernamee}",bg='#8B8378' ,font=('Helvetica', 20)).place(relx=0.27,rely=0.21,anchor=CENTER)
        Label(master, text="Player List:",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=0.25,anchor=CENTER)
        Label(master, text="=======================================================",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=0.30,anchor=CENTER)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(relx=0.5,rely=0.14,anchor=CENTER)
        waiting = threading.Thread(target=self.UpdateList)
        waiting.start()
    def UpdateList(self):
        blah = 0.35
        countt = 0
        runninggg = True
        ffjff = []
        while runninggg == True:
            try:
                for item in players_database:
                    if item != "deleted":
                        if item != "New":
                            if item not in ffjff:
                                print(item)
                                PLayernamee = Label(self.master, text=f"Player Name: {item}",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=blah,anchor=CENTER)
                                blah += 0.05
                                print("Appending " + item)
                                time.sleep(1)
                                print("Destroying")
                                ffjff.append(item)
                                print("Finished")
            except RuntimeError:
                pass
    def StartGame(self):
        #start game here
        pass
    def Quitbtn(self):
        searchingg = False
        endserver = True
        self.master.destroy()
class SettingUpGUI:
    def __init__(self,master):
        self.master = master
        master.geometry('597x588')
        master.configure(background='#8B8378')
        master.title('Main Menu')
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(x=362, y=570)
        Label(master, text='Server Setup', bg='#8B8378', font=('verdana', 30, 'bold')).place(x=146, y=101)
        Label(master, text='Name Of Classroom:', bg='#8B8378', font=('verdana', 10, 'normal')).place(x=148, y=258)
        self.name = nameofserver=Entry(master)
        self.name.place(x=149, y=282)
        Label(master, text='Level of hardness', bg='#8B8378', font=('verdana', 10, 'normal')).place(x=149, y=331)
        self.levelofhardness=Listbox(master, bg='#CDC0B0', font=('verdana', 10, 'normal'), width=0, height=0)
        self.levelofhardness.insert('0', 'easy')
        self.levelofhardness.insert('1', 'medium')
        self.levelofhardness.insert('2', 'hard')
        self.levelofhardness.place(x=152, y=354)
        Button(master, text='Start Server', bg='#CDC0B0', font=('verdana', 10, 'normal'), command=self.startserver).place(x=152, y=431)
    def Servername_value(self):
        userInput = self.name.get()
        return userInput
    def LOH_value(self):
        itemSelected = self.levelofhardness.curselection()
        return itemSelected
    def startserver(self):
        #####Start Server Here=======================================
        #####Start Server Here=======================================
        #####Start Server Here=======================================
        print('clicked')
        global servername
        servername = str(self.Servername_value())
        global LOH
        LOH = str(self.LOH_value)
        self.master.destroy()
        serverroot = Tk()
        global lobby_gui
        lobby_gui = LobbyGUI(servername,LOH,port,serverroot)
        serverroot.mainloop()
    
port = random.randint(10000,65535)
print (host)
print (port)
print(servername)
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
        global endserver
        while endserver == False:
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
        while StartServer == True:
                datafromplayer = self.sock.recv(1024).decode()
                nameinb = b = self.name.encode('utf-8')
                servernameinb = b = servername.encode('utf-8')


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
            print(f"---- Port: {port}")
            print(f"---- Server Name: {servername}")
            print("---- Players")
            for item in players_database:
                if item != "deleted" or item != "New":
                    print(f"- {item}")
            print("============================================")
            print(lobby_gui)
            lobby_gui.UpdateList()
            time.sleep(5)

serversocket.listen(5)
print ('server started and listening')
def SearchingForPlayers(fvvtvttgt=False):
    print("Hey it opened")
    searchingg = True
    while searchingg == True:
        print("Checking for PLAYERS")
        clientsocket, address = serversocket.accept()
        AddPlayer("New",0,clientsocket, address)
    return
    print("END")
searching = threading.Thread(target=SearchingForPlayers)
searching.start()
class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        Label(master, text='Math Race!', bg='#8B8378', font=('helvetica', 30, 'bold')).place(x=175, y=94)
        Button(master, text='Play', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.NextMenu).place(x=219, y=302)
        Button(master, text='Quit', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(x=218, y=402)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(x=362, y=570)
    def NextMenu(self):
        self.master.destroy()
        roott = Tk()
        my_gui = SettingUpGUI(roott)
        roott.mainloop()
    def Quitbtn(self):
        self.master.destroy()

root = Tk()
my_gui = MainMenu(root)
root.mainloop()