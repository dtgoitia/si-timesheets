import json
import errno
import os
from pathlib import Path


DEFAULT_FILE_PATH = str(Path(Path.home(), '.sit/.config'))


def get_config(file_path=DEFAULT_FILE_PATH) -> dict:
    """Import JSON configuration.

    If no file path is provided, try to import from the default
    path `~/.sit/.config`
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_path)
    with open(file_path) as fd:
        config = json.load(fd)
        return config
