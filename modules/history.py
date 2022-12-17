import os
from pathlib import Path

filename = f"{str(Path.home())}/.pywinterminal/history.txt"


def parse(input_command: str) -> str:
    """Returns and parses predefined commands and history for console

    Args:
        input_command (str): input tommcand

    Returns:
        str
    """
    # reads history file
    history = read_history()

    # parses !! from the command if user enters a number from history similar to bash shell
    if "!!" in input_command:
        input_command = history[int(input_command.replace("!!", ""))]

    # if exit is typed exit gracefully
    if "exit" in input_command:
        exit()

    # clears history
    if "clear" in input_command:
        os.remove(filename)

    return input_command


def create_history() -> bool:
    """Creates history file

    Returns:
        bool: True or False
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        open(filename, "w")
        return True
    except:
        return False


def append_history(history: str) -> bool:
    """Appends history to file

    Args:
        history (str): command history entry

    Returns:
        bool: True or False
    """
    try:
        file = open(filename, "a")
        file.write(f"{history} \n")
        return True
    except:
        return False


def read_history() -> list:
    """Opens file history

    Returns:
        list
    """
    try:
        if Path(filename).is_file():
            return open(filename).readlines()
        else:
            return create_history()
    except:
        return []
