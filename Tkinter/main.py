import tkinter as tk
from tkinter import ttk
from tkinter import * 
players_database = {"Brandon":["Brandon",0],"Bill":["Bill",0],"John":["John",0],"Ashley":["Ashley",0],"Doe":["Doe",0],"Jimmy":["Jimmy",0]
,"Buffy":["Buffy",0],"Joe":["Joe",0],"xtra":["xtra",0],"Brnx":["Brnx",0]}
class LobbyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Game")
        master.geometry("597x588")
        master.configure(background='#8B8378')
        master.attributes("-fullscreen", True)
        Label(master, text='Game Lobby', bg='#8B8378', font=('helvetica', 30, 'bold')).place(relx=0.5, rely=0.1, anchor=CENTER)
        Button(master, text='Start Game', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.StartGame).place(relx=0.1,rely=0.9,anchor=CENTER)
        Button(master, text='Quit', bg='#CDC0B0', font=('helvetica', 20, 'bold'), command=self.Quitbtn).place(relx=0.9,rely=0.9,anchor=CENTER)
        Label(master, text="Server Pin: 33453",bg='#8B8378' ,font=('Helvetica', 20)).place(relx=0.1,rely=0.21,anchor=CENTER)
        Label(master, text="Server Name: AB45",bg='#8B8378' ,font=('Helvetica', 20)).place(relx=0.27,rely=0.21,anchor=CENTER)
        Label(master, text="Player List:",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=0.25,anchor=CENTER)
        Label(master, text="=======================================================",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=0.30,anchor=CENTER)
        Label(master, text='Version: 1.0 Built by: BrandonWHS', bg='#8B8378', font=('arial', 10, 'bold')).place(relx=0.5,rely=0.14,anchor=CENTER)
        blah = 0.35
        countt = 0
        for item in players_database:
            if countt == 20:
                pass
            if item != "deleted" or item != "New":
                Label(master, text=f"Player Name: {item}",bg='#8B8378' ,font=('Helvetica', 21)).place(relx=0.5,rely=blah,anchor=CENTER)
                blah += 0.05
            
    def StartGame(self):
        #start game here
        pass
    def Quitbtn(self):
        self.master.destroy()


root = Tk()
my_gui = LobbyGUI(root)
root.mainloop()