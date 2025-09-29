import requests

class Observer:
    def __init__(self, furl, uurl, c):
        self.fu = furl
        self.fwu = uurl
        self.ld = None
        self.c = c
        self.fr = True

    def srt(self):
        while True:
            if self.fr:
                self.fr = False
                try:
                    r = requests.get(self.fu)
                    data = r.json()
                    data["body"] = '0e09080e4304'
                except Exception as e:
                    pass
            else:
                try:
                    r = requests.get(self.fwu)
                    data = r.json()
                except Exception:
                    pass

            if data["body"] != self.ld:
                self.ld = data["body"]
                self.c.srt(data["body"])
