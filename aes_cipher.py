import hashlib,base64,os
from Crypto.Cipher import AES
from Crypto import Random
SZ=16
def pad(s):
    padlen=SZ-len(s)%SZ
    ans=chr(padlen)*padlen
    return s+ans
def unpad(s):
    padlen=s[-1]
    return s[:-padlen]
def encrypt(msg,key):
    try:
        pkey=hashlib.sha256(key.encode()).digest()
        msg=pad(msg)
        plain_bytes=msg.encode()
        iv=Random.new().read(AES.block_size)
        cipher=AES.new(pkey,AES.MODE_CBC,iv)
        byte=cipher.encrypt(plain_bytes)
        ans=base64.b64encode(iv+byte).decode()
        return ans
    except Exception:
        print("Cannot encrypt the message. the connection will be closed due to security concerns")
        os._exit(0)
        return "exit..."
def decrypt(msg,key):
    try:
        pkey=hashlib.sha256(key.encode()).digest()
        cipher_bytes=base64.b64decode(msg)
        iv=cipher_bytes[:16]
        cipher=AES.new(pkey,AES.MODE_CBC,iv)
        byte=cipher.decrypt(cipher_bytes[16:])
        ans=unpad(byte)
        return ans.decode()
    except Exception:
        print("Cannot decrypt the message. the connection will be closed due to security concerns")
        os._exit(0)
        return "exit..."