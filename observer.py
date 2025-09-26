import requests
import time

class Observer:
    def __init__(self, first_url, url_with_username, client, interval=1):
        self.first_url = first_url
        self.url_with_username = url_with_username
        self.interval = interval
        self.last_data = None
        self.client = client
        self.first_run = True

    def start(self):
        while True:
            if self.first_run:
                self.first_run = False
                try:
                    response = requests.get(self.first_url)
                    data = response.json()
                    data["body"] = '0e09080e4304'
                except Exception as e:
                    print(f"Erro ao buscar URL: {e}")
                    time.sleep(self.interval)
            else:
                try:
                    response = requests.get(self.url_with_username)
                    data = response.json()
                except Exception as e:
                    print(f"Erro ao buscar URL: {e}")
                    time.sleep(self.interval)

            if data["body"] != self.last_data:
                self.last_data = data["body"]
                self.client.start(data["body"])

            time.sleep(self.interval)
