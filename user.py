class User:
    def __init__(self,a,b,c,d):
        self.firstname=a
        self.lastname=b
        self.username=c
        self.address=d
        self.ip,self.port=d.split("/")
        with open(f"temp.txt","w") as f:
            f.write(self.firstname+"\n")
            f.write(self.lastname+"\n")
            f.write(self.username+"\n")
            f.write(self.address)
    def edit_firstname(self,a):
        self.firstname=a
        with open(f"temp.txt","w") as f:
            f.write(self.firstname+"\n")
            f.write(self.lastname+"\n")
            f.write(self.username+"\n")
            f.write(self.address)
    def edit_lastname(self,a):
        self.lastname=a
        with open(f"temp.txt","w") as f:
            f.write(self.firstname+"\n")
            f.write(self.lastname+"\n")
            f.write(self.username+"\n")
            f.write(self.address)
    def edit_username(self,a):
        self.username=a
        with open(f"temp.txt","w") as f:
            f.write(self.firstname+"\n")
            f.write(self.lastname+"\n")
            f.write(self.username+"\n")
            f.write(self.address)
    def edit_address(self,a):
        self.address=a
        self.ip,self.port=a.split("/")
        with open(f"temp.txt","w") as f:
            f.write(self.firstname+"\n")
            f.write(self.lastname+"\n")
            f.write(self.username+"\n")
            f.write(self.address)
    def __str__(self):
        return "first name: "+self.firstname+" lastname: "+self.lastname+"\nusername: "+self.username+" address: "+self.address

