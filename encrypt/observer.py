import requests

class Observer:
    def __init__(self, furl, uurl, client):
        self.first_url = furl
        self.url_with_username = uurl
        self.last_data = None
        self.client = client
        self.first_run = True

    def srt(self):
        while True:
            if self.first_run:
                self.first_run = False
                try:
                    response = requests.get(self.first_url)
                    data = response.json()
                    data["body"] = '0e09080e4304'
                except Exception as e:
                    pass
            else:
                try:
                    response = requests.get(self.url_with_username)
                    data = response.json()
                except Exception as e:
                    pass

            if data["body"] != self.last_data:
                self.last_data = data["body"]
                self.client.srt(data["body"])
