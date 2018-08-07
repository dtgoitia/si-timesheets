import json


def get_config(file_path: str) -> dict:
    """Import JSON configuration."""
    with open('.config') as fd:
        config = json.load(fd)
        return config
