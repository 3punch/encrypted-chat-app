import user,socket,threading,os,datetime,time,random
from aes_cipher import encrypt,decrypt
users=[]
allmsg=[]
key="11228"
def send_server():
    while True:
        msg=input()
        if msg=="exit":
            cmd=input("save? (y/n) ")
            if cmd=="y":
                saver()
            func("exit...")
            func(f"Connection closed with user {user.username}")
            os._exit(0)
        if msg=="getinfo":
            func("info:")
        elif msg=="save":
            saver()
        else:
            msg=f"[{user.username}]:{msg}"
            allmsg.append(msg)
            func(msg)
def saver():
    filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt"
    with open(filename,"x") as saved:
        for s in allmsg:
            saved.write(s+"\n")
def func(msg,sender=None):
    for i in users:
        try:
            if i!=sender:
                aesmsg=encrypt(msg,key).encode()
                i.sendall(aesmsg)
        except:
            users.remove(i)
def dojob(s):
    while True:
        try:
            msg=s.recv(1024)
            if not msg:
                cnt=0
                flag=False
                while cnt<120:
                    cnt+=5
                    time.delay(5)
                    newsocket,_addr=s.accept()
                    if newsocket!=None:
                        print("Reconnected")
                        flag=True
                        users.append(newsocket)
                        break
                if flag==False:
                    break
                else:
                    threading.Thread(target=sendallmsg,args=(s,)).start()
            aesmsg=decrypt(msg.decode(),key)
            if aesmsg=="exit...":
                os._exit(0)
            if aesmsg=="info:":
                tmp=f"name: {user.firstname} {user.lastname}\nusername: {user.username}\nip: {user.ip}\nport: {user.port}"
                func(tmp)
                continue
            allmsg.append(aesmsg)
            print(aesmsg)
            func(f"[{user.username}]: {aesmsg}",s)
        except:
            break

def recvive(sock):
    while True:
        try:
            msg=sock.recv(1024)
            if not msg:
                cnt=0
                flag=False
                while cnt<120:
                    cnt+=5
                    time.delay(5)
                    newsocket,_addr=sock.accept()
                    if newsocket!=None:
                        print("Reconnected")
                        flag=True
                        users.append(newsocket)
                        break
                if flag==False:
                    break
                else:
                    threading.Thread(target=sendallmsg,args=(sock,)).start()
            aesmsg=decrypt(msg.decode(),key)
            if aesmsg=="info:":
                sockstr=f"name: {user.firstname} {user.lastname}\nusername: {user.username}\nip: {user.ip}\nport: {user.port}"
                encrypted_sockstr=encrypt(sockstr,key).encode()
                sock.sendall(encrypted_sockstr)
                continue
            allmsg.append(aesmsg)
            print(aesmsg)
        except:
            break
def sendallmsg(s):
    for i in allmsg:
        s.sendall(encrypt(i,key).encode())
a1=input("Enter your firstname:\t")
a2=input("Enter your lastname:\t")
a3=input("Enter your username:\t")
a4=input("Enter your address: (ip/port)\t")
user=user.User(a1,a2,a3,a4)
while True:
    cmd=input("Edit? y/n ")
    if cmd=="n":
        break
    elif cmd!="y":
        print("Wrong command")
        continue
    cmd=input("Which part?(firstname|lastname|username|address)")
    new=input("Enter your new information:\t")
    if cmd=="firstname":
        user.edit_firstname(new)
    elif cmd=="lastname":
        user.edit_lastname(new)
    elif cmd=="username":
        user.edit_username(new)
    elif cmd=="address":
        user.edit_address(new)
    else:
        print("Wrong command")
        continue
print(user)
with open(f"information.txt","a") as f:
    f.write(user.firstname+"\n")
    f.write(user.lastname+"\n")
    f.write(user.username+"\n")
    f.write(user.address+"\n")
s=input("Room creator? y/n ")
if s=="n":
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip=input("Enter server IP:")
    port=8080
    mysocket.connect((ip,port))
    threading.Thread(target=recvive,args=(mysocket,)).start()
    while True:
        msg=input()
        if msg=="exit":
            cmd=input("save? (y/n)")
            if cmd=="y":
                saver()
            mysocket.sendall(encrypt(f"Connection closed with user {user.username}",key).encode())
            os._exit(0)
        if msg=="getinfo":
            mysocket.sendall(encrypt("info:",key).encode())
            continue
        elif msg=="save":
            saver()
            continue
        msg=f"[{user.username}]:{msg}"
        allmsg.append(msg)
        mysocket.sendall(encrypt(msg,key).encode())
elif s=="y":
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip="0.0.0.0" #user.ip 
    port=8080
    mysocket.bind((ip,port))
    mysocket.listen()
    print("Ready for connection !")
    threading.Thread(target=send_server).start()
    while True:
        newsocket,_addr=mysocket.accept()
        print("Connected")
        users.append(newsocket)
        threading.Thread(target=dojob,args=(newsocket,)).start()
        threading.Thread(target=sendallmsg,args=(newsocket,)).start()
else:
    print("Wrong command connection closed :(")
