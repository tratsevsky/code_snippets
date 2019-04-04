import paramiko
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.1.10', port=22, username='user', password='cisco', look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('show version')
# stdin, stdout, stderr = ssh_client.exec_command('show version', get_pty=True)
# stdin.write('mypass123\n') for commands with sudo in linux
# print(stderr.read().decode())
output = stdout.read().decode()
print(output)

ssh_client.close()

with open('R1_show_version.txt', 'w') as f:
    f.write(output)
