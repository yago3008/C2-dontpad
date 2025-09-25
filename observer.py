import requests
import time

class Observer:
    def __init__(self, url, client, interval=2):
        self.url = url
        self.interval = interval
        self.last_data = None
        self.client = client  # cliente que será acionado quando mudar

    def start(self):
        while True:
            try:
                response = requests.get(self.url)
                data = response.json()
            except Exception as e:
                print(f"Erro ao buscar URL: {e}")
                time.sleep(self.interval)
                continue

            if data["body"] != self.last_data:
                self.last_data = data["body"]
                print("Conteúdo alterado! Acionando client...")
                self.client.execute_command(data["body"])
            else:
                print("Sem alteração, aguardando...")

            time.sleep(self.interval)
