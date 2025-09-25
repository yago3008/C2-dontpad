import requests
import time
import sys
from criptographer import Criptographer
import getpass

if __name__ == "__main__":
    command = sys.argv[1]
    data = {
    "text": Criptographer.encrypt(command+'\n___________________\n\n', getpass.getuser()),
    "lastModified": int(time.time() * 1000),
    "force": "true",
    "session-token": "-25751fc88e6e559870fd"
}

    response = requests.post("https://api.dontpad.com/yaguinhofodinha/yago.martins", data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")