import subprocess


def user_input_command(computername: str, pwd: str):
    """Reads user command input

    Args:
        computername (str): computername to display in terminal

    Returns:
        str: input_command
    """
    if pwd == "":
        pwd = "NoCurrentDirectory"
    input_command = input(f"{computername} > {pwd} > ")
    return input_command


def execute_user_input_command(
    computername: str, command: str, username: str, password: str, pwd: str
) -> str:
    """Executes command on remote machine

    Args:
        computername (str): computername to execute remote command on
        command (str): command to execute
    """
    output = (
        subprocess.run(
            [
                "scripts/pwshrc.sh",
                "-c",
                command,
                "-s",
                computername,
                "-u",
                username,
                "-p",
                password,
                "-w",
                pwd,
            ],
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .splitlines()
    )
    output = [out for out in output if out != ""]
    output.pop(0)
    for out in output:
        print(out)

    working_directory = output[-1]
    return working_directory  # working directory that is outputed at the end of the command
