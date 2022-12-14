import subprocess


def user_input_command(computername: str):
    """Reads user command input

    Args:
        computername (str): computername to display in terminal

    Returns:
        str: input_command
    """
    input_command = input(f"{computername} :: pywinterminal>>> ")
    return input_command


def execute_user_input_command(computername: str, command: str):
    """Executes command on remote machine

    Args:
        computername (str): computername to execute remote command on
        command (str): command to execute
    """
    subprocess.run(
        ["scripts/pwshrc.sh", "-c", command, "-s", computername, "-i", "0"]
    ).stdout
