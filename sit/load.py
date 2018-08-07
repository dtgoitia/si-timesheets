import json


def get_config(file_path: str) -> dict:
    with open('.config') as fd:
        config = json.load(fd)
        return config
