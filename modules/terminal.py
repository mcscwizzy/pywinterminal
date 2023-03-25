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
        username (str): username to connect to machine
        password (str): password for username
        pwd (sr): parent working directory
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

    # remove empty spaces in list
    output = [out for out in output if out != ""]

    # if an error happened we want this last line replaced with the last pwd
    if "FullyQualifiedErrorId" in output[-1]:
        working_directory = pwd
    else:
        # if there is no erro then contine as normal
        working_directory = output[-1]

    # remove first entry which is the computer name
    output.pop(0)

    # print results to terminal
    for out in output:
        print(out)

    # return the working directory
    return working_directory  # working directory that is outputed at the end of the command
