import socket
import time
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.207.74"
checkingforerror = True
while checkingforerror == True:
    try:
        print("Hello!")
        port = int(input("What your 5 number pin?"))
        s.connect((host,port))
        checkingforerror = False
    except:
        print("Invalid try again.")
def WaitingLobby():
    gamestarted = False
    while gamestarted == False:
        print("Waiting")
        time.sleep(5)
 
def sendname(name):
   s.send(name.encode())
   data = ''
   data = s.recv(1024).decode()
   print (data)
   WaitingLobby()
 
namenotsend = True
while namenotsend == True:
    r = input('enter name please')
    sendname(r)
    namenotsend = False
 
s.close ()