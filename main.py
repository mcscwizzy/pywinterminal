import argparse
from modules.pywinterminal import *


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

    start(computername, username, password)


if __name__ == "__main__":
    main()
