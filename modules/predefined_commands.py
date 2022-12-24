import os
from pathlib import Path
from modules.history import read_history

filename = f"{str(Path.home())}/.pywinterminal/history.txt"


def parse_commands(input_command: str) -> bool:
    """Checks for predefined commands

    Args:
        input_command (str): command from terminal
    """
    predefined_command = False
    if "exit" in input_command:
        exit()

    if "clear" in input_command:
        predefined_command = True
        os.remove(filename)

    if "history" in input_command:
        predefined_command = True
        i = 0
        history = read_history()
        for line in history:
            i = i + 1
            print("{0} {1}".format(i, str(line).replace("\n", "")))

    return predefined_command
