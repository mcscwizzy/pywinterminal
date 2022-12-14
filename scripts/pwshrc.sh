#!/bin/bash

while getopts ":c:s:i:" opt; do
  case $opt in
    c) command="$OPTARG"
    ;;
    s) server="$OPTARG"
    ;; 
  esac
done

if [ -z "$command" ] || [ -z "$server" ] ; then
  echo "-c command -s server -i index"
else
  ansible_password=your_username
  ansible_username=p@55w0rd
  ansible_environment='{"ansible_connection": "winrm", "ansible_port": "5985", "ansible_winrm_scheme": "http", "ansible_winrm_server_cert_validation": "ignore", "ansible_winrm_transport": "ntlm", "ansible_user": "'$ansible_username'", "ansible_password": "'$ansible_password'"}'
  ansible all -m "win_shell" -a "$command" -i "$server," -e "$ansible_environment"
fi











