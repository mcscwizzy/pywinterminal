import argparse
from modules.pywinterminal import *


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--computername",
        help="The computername of the client you wish to connect to.",
    )
    parser.add_argument(
        "--username", help="Username used to connect to the computername."
    )
    parser.add_argument("--password", help="Password used with the username")
    args = parser.parse_args()

    computername = args.computername
    username = args.username
    password = args.password

    start(computername, username, password)


if __name__ == "__main__":
    main()
