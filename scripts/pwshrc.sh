#!/bin/bash

while getopts ":c:s:u:p:w:" opt; do
  case $opt in
    c) command="$OPTARG"
    ;;
    s) server="$OPTARG"
    ;;
    u) username="$OPTARG"
    ;;
    p) password="$OPTARG"
    ;;
    w) pwd="$OPTARG"
    ;;              
  esac
done

if [ -z "$command" ] || [ -z "$server" ] || [ -z "$username" ] || [ -z "$password" ]; then
  echo "-c command -s server -u username -p password"
else
  ansible_environment='{"ansible_connection": "winrm", "ansible_port": "5985", "ansible_winrm_scheme": "http", "ansible_winrm_server_cert_validation": "ignore", "ansible_winrm_transport": "ntlm", "ansible_user": "'$username'", "ansible_password": "'$password'"}'
  ansible all -m "win_shell" -a "cd $pwd; $command; (pwd).Path" -i "$server," -e "$ansible_environment"
fi











