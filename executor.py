import requests
import time
import sys


if __name__ == "__main__":
    command = sys.argv[1]
    data = {
    "text": command,
    "lastModified": int(time.time() * 1000),
    "force": "true",
    "session-token": "-25751fc88e6e559870fd"
}

    response = requests.post("https://api.dontpad.com/yaguinhofodinha", data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")