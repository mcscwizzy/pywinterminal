# pywinterminal

Pywinterminal allows you to execute remote commands on a Windows machine from an interactive terminal on a Mac or Linux box!

# Intro

This is a project that started as more of a need than a side project. I migrated over to Linux and Mac from Windows, but still have to remote into Windows servers on occasion. I got tired of having to RDP into a Windows box everytime when all I needed was a simple piece of information, or a simple command to execute. While SSH can be put on Windows boxes it is not widely supported yet and WinRM is still
the default way to remotely communicate and send commands to Windows.

# How does it work

Instead of reinventing the wheel I decided to use what I had, and that was Ansible. Ansible does a great job of communicating with Windows boxes via pywinrm and can execute adhoc commands. That is exactly what this does. While this is not a true TTY terminal it allows you to keep entering commands while maintaining a mock session. It's not perfect, but it works!

# Caution

This project is in very early stages. The code is not optimzied and it was just something I threw together while I was thinking of it.
All of this is on my todo list and will only get better.

# How to use

1. Install python 3.11
2. Make sure you have Ansible installed
3. Enter your username and password for the Windows box you are connecting to in the pwshrc.sh file
4. Run `python main.py windowsserver.domain.com` or `python main.py windowsserver.domain.com,windowsserver2.domain.com` as
   it can run commands on multiple hosts at the same time
5. This will open a mock terminal. You can put any Powershell command you want including piped commands as well. Then press ENTER
6. It will then send the command to the Windows box if everything is configured correctly
7. After the command has ran you will be back at the terminal ready to type another command. History is collected at the top.
8. Type `exit` to exit or `clear` to clear history
9. You can type `!!1` or replace whatever number is on the history for the command you want to run to execute

# Future additions

1. Credential manager
2. Logging command history to file
3. Removing the Ansible type output and make it more Powershell like.
4. Parameter names for main.py with help file
5. Uploading to Pypi
6. Intelliegence to be directory aware of when you send commands so when you `cd` to a directory and you send another command
   it will tack on that directory structure for you just like you were at the terminal of the machine itself.
