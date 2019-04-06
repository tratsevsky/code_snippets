import helper_paramiko
import getpass

password = getpass.getpass()

# This is snippet for connecting to Linux server

ssh_client = helper_paramiko.connect('192.168.0.133', 2299, 'linuxadmin', password)
remote_connection = helper_paramiko.get_shell(ssh_client)

helper_paramiko.send_command(remote_connection, 'sudo useradd -m -d /home/user1 -s /bin/bash user1')
helper_paramiko.send_command(remote_connection, password) # sudo password, supposed to be the same as
users = helper_paramiko.send_command(remote_connection, 'cat /etc/passwd')

print(users.decode())

helper_paramiko.close(ssh_client)