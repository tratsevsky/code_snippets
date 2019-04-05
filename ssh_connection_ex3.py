import helper_paramiko

ssh_client = helper_paramiko.connect('10.1.1.10', 22, 'admin', 'cisco')
remote_connection = helper_paramiko.get_shell(ssh_client)

helper_paramiko.send_command(remote_connection, 'enable')
helper_paramiko.send_command(remote_connection, 'cisco')
helper_paramiko.send_command(remote_connection, 'terminal length 0')

output = helper_paramiko.send_command(remote_connection, 'show run')
print(output.decode())

helper_paramiko.close(ssh_client)