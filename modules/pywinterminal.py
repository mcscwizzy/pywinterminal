from modules.terminal import *
from modules.history import *
from modules.predefined_commands import *


def start(computername: str, username: str, password: str) -> None:
    """Starts the tty terminal session

    Args:
        computername (str): computername to connect to
        username (str): username used to connect to computername
        password (str): password for username
    """

    # parent working directory to keeping directory state throughout the terminal session
    pwd = ""

    while True:

        # set variable to remember command history
        history = read_history()

        # gathers user input
        input_command = user_input_command(computername, pwd)

        # parse history and predefined commands
        if input_command:
            if "!!" in input_command:
                input_command = parse_history(input_command=input_command)
                execute_user_input_command(
                    computername, input_command, username, password
                )
            else:
                if not parse_commands(input_command=input_command):
                    working_direectory = execute_user_input_command(
                        computername, input_command, username, password, pwd
                    )

            # append to history only if the command doesn't exist already
            if input_command not in history and "clear" not in input_command:
                append_history(input_command)

            # we want the pwd updated with the new working directory to be passed in next time the command runs
            pwd = working_direectory
