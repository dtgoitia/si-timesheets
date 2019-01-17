import json
import os


DEFAULT_FILE_PATH = os.path.join(os.path.expanduser('~'), '.config', 'sit', '.config')


def get_config(file_path=DEFAULT_FILE_PATH) -> dict:
    """Import JSON configuration.

    If no file path is provided, try to import from the default
    path `~/.config/sit/.config`
    """
    with open(file_path) as fd:
        config = json.load(fd)
        return config
