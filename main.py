from modules.terminal import *
from modules.history import *
from modules.predefined_commands import *
import sys, argparse


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--computerName", help="The computername of the client you wish to connect to."
    )
    parser.add_argument("--userName", help="Username used to connect to the client.")
    parser.add_argument("--password", help="Password used with the username")
    args = parser.parse_args()

    computername = args.computerName
    username = args.userName
    password = args.password
    pwd = ""

    # this is a forever loop to keep the console "open"
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

            pwd = working_direectory


if __name__ == "__main__":
    main()
