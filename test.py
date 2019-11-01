import inspect
import Domain
import test2
import json

if __name__ == "__main__":
    with open("config.json") as f:
        print(json.load(f))
