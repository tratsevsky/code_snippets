import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.1.10', port=22, username='user', password='cisco', look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

#copy a single file (destination will be overwritten!!!)
scp.put('devices.txt', 'aaa.txt')

#copy a directory
scp.put('directory1', recursive=True, remote_path='/tmp')

# scp get remote file
scp.get('/etc/passwd', 'passwd')
scp.get('/etc/passwd1', 'C:\\Users\\alexander\\passwd1')

scp.close()


