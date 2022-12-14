import sys
from modules.terminal import *


def main():
    # set variable to remember command history
    history = ["<< Command History >>"]

    # computer name entered from the console
    computername = sys.argv[1]

    # this is a forever loop to keep the console "open"
    while True:
        if len(history) > 1:

            # we do not want the index of command history so we only print the entry in the list
            for command in history:
                if "Command History" in command:
                    print(command)
                # this prints the index so we can pass that into the command prompt to repeat commands
                else:
                    print(f"{history.index(command)}. {command}")
        # spacer
        print("")

        # gathers user input
        input_command = user_input_command(computername=computername)

        # parses !! from the command if user enters a number from history similar to bash shell
        if "!!" in input_command:
            input_command = history[int(input_command.replace("!!", ""))]

        # if exit is typed exit gracefully
        if "exit" in input_command:
            exit()

        # clears history
        if "clear" in input_command:
            history = ["<< Command History >>"]

        # execute command
        execute_user_input_command(
            computername=sys.argv[1],
            command=input_command,
        )

        # append to history only if the command doesn't exist already
        if input_command not in history and "clear" not in input_command:
            history.append(input_command)


if __name__ == "__main__":
    main()