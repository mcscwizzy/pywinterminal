# pywinterminal

Pywinterminal allows you to execute remote commands on a Windows machine from an interactive terminal on a Mac or Linux box!

# Intro

This is a project that started as more of a need than a side project. I migrated over to Linux and Mac from Windows, but still have to remote into Windows servers on occasion. I got tired of having to RDP into a Windows box everytime when all I needed was a simple piece of information, or a simple command to execute. While SSH can be put on Windows boxes it is not widely supported yet and WinRM is still
the default way to remotely communicate and send commands to Windows.

# How does it work

Instead of reinventing the wheel I decided to use what I had, and that was Ansible. Ansible does a great job of communicating with Windows boxes via pywinrm and can execute adhoc commands. That is exactly what this does. While this is not a true terminal it allows you to keep entering commands while maintaining a mock session. 

Terminal maintains directory awareness. If you type `cd c:\temp` it will change into that directory, and maintain that you are in that directory next time you run a command. So it will feel like you are at a Powershell prompt running commands!

# Caution

This project is in very early stages. The code is not optimzied and it was just something I threw together while I was thinking of it.
All of this is on my todo list and will only get better.

# How to use

1. Install python 3.11
2. Make sure you have Ansible installed
3. Run `python main.py --copmuterName computer1 --username username --password password1` 
4. This will open a mock terminal. You can put any Powershell command you want including piped commands as well. Then press ENTER
5. It will then send the command to the Windows box if everything is configured correctly
6. After the command has ran you will be back at the terminal ready to type another command.
7. Type `exit` to exit or `clear` to clear history or `history` to view history
8. You can type `!!1` or replace whatever number is on the history for the command you want to run to execute
9.  History is stored in userprofile/.pywintermina/history.txt

