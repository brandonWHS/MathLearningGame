import tkinter as tk
from tkinter import ttk
from tkinter import *
import socket
import time
from tkinter.constants import ANCHOR, CENTER
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port = 0
class WaitingGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Game | Waiting")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Now wait.', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5,rely=0.5,anchor=CENTER)
    def NextMenu(self):
        pass
    def Quitbtn(self):
        self.master.destroy()
def sendname(name):
    s.send(name.encode())
    data = ''
    data = s.recv(1024).decode()
    rooooot = Tk()
    nextlevel = WaitingGUI(rooooot)
    root.mainloop()
   
class Options_nameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Name Selection', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5,rely=0.1,anchor=CENTER)
        Label(master, text='Please Enter your name.', bg='#8B8378', font=('helvetica',18)).place(relx=0.36,rely=0.5,anchor=CENTER)
        Button(master, text='Join', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.NextMenu).place(relx=0.5,rely=0.56,anchor=CENTER)
        Button(master, text='Back', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(relx=0.5,rely=0.64,anchor=CENTER)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(relx=0.5,rely=0.15,anchor=CENTER)
        self.name=Entry(master,font=(10),width=6,)
        self.name.place(relx=0.497,rely=0.5,anchor=CENTER)
    def NextMenu(self):
        #Sending Name
        #==============================
        sendname(str(self.name.get()))
        self.master.destroy()
    def Quitbtn(self):
        self.master.destroy()
class OptionsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Starting Server.', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5,rely=0.1,anchor=CENTER)
        Label(master, text='Please Enter the Server Code:', bg='#8B8378', font=('helvetica',18)).place(relx=0.36,rely=0.5,anchor=CENTER)
        Button(master, text='Join', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.NextMenu).place(relx=0.5,rely=0.56,anchor=CENTER)
        Button(master, text='Quit', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(relx=0.5,rely=0.64,anchor=CENTER)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(relx=0.5,rely=0.15,anchor=CENTER)
        self.serverpin=Entry(master,font=(10),width=6,)
        self.serverpin.place(relx=0.497,rely=0.5,anchor=CENTER)
        self.errormessage1 = Label(master, text=f"Error: Your Pin is incorrect!, Try Again", bg='#FF0000', font=('arial',10,'bold'))
        self.errormessage2 = Label(master, text=f"Error: Your username, Has already been taken, Try again", bg='#FF0000', font=('arial',10,'bold'))
    def ErrorAppeared(self,whaterror):
        if whaterror == "pin":
            self.errormessage1.place(relx=0.5,rely=0.41,anchor=CENTER)
        else:
            self.errormessage2.place(relx=0.5,rely=0.41,anchor=CENTER)
    def Serverport_value(self):
        userInput = str(self.serverpin.get())
        return userInput
    def NextMenu(self):
        checkingforerror = True
        print("Made it")
        print("Made it")
        global port
        port = self.Serverport_value()
        print(f"port is: {port}")
        try:
            s.connect((host,port))
        except:
            self.ErrorAppeared("pin")
            return
        print("passed")
        checkingforerror = False
        print("Made it")
        roooot = Tk()
        nextlevel = Options_nameGUI(roooot)
        self.master.destroy()
        print("Made it")
        root.mainloop()
        print("Made it")
        
    def Quitbtn(self):
        self.master.destroy()
class StartGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Math Race!', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5,rely=0.1,anchor=CENTER)
        Button(master, text='Play', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.NextMenu).place(relx=0.5,rely=0.5,anchor=CENTER)
        Button(master, text='Quit', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(relx=0.5,rely=0.6,anchor=CENTER)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(relx=0.5,rely=0.15,anchor=CENTER)
    def NextMenu(self):
        rooot = Tk()
        nextlevel = OptionsGUI(rooot)
        self.master.destroy()
        root.mainloop()
    def Quitbtn(self):
        self.master.destroy()

root = Tk()
my_gui = StartGUI(root)
root.mainloop()
