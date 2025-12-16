import json
from datetime import datetime

FILE_NAME = "daily.json"


def save_daily(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(FILE_NAME, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = {}

    history[timestamp] = data

    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)


def load_daily():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
