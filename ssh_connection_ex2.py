import paramiko
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.1.10', port=22, username='user', password='cisco', look_for_keys=False, allow_agent=False)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('enable\n')
remote_connection.send('cisco\n')
remote_connection.send('config t\n')
remote_connection.send('interface lo0\n')
remote_connection.send('ip address 1.1.1.1 255.255.255.255\n')
remote_connection.send('int lo1\n')
remote_connection.send('ip address 2.2.2.2 255.255.255.255\n')
remote_connection.send('router ospf 1\n')
remote_connection.send('network 0.0.0.0 0.0.0.0 area 0\n')
remote_connection.send('end\n')

import time
time.sleep(3)

output = remote_connection.recv(4096)
print(output.decode())

ssh_client.close()


