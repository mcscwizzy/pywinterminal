import sys
from modules.terminal import *
from modules.history import *


def main():

    computername = sys.argv[1]

    # this is a forever loop to keep the console "open"
    while True:

        # set variable to remember command history
        history = read_history()

        # gathers user input
        input_command = user_input_command(computername)

        # parse user commands
        input_command = parse(input_command)

        # execute command
        execute_user_input_command(computername, input_command)

        # append to history only if the command doesn't exist already
        if input_command not in history and "clear" not in input_command:
            append_history(input_command)


if __name__ == "__main__":
    main()
