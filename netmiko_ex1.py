from netmiko import Netmiko
from netmiko import ConnectHandler

# connection = Netmiko(host='10.1.1.10', username='u1', password='cisco', device='cisco_ios')

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
#output = connection.send_command('show ip int br')
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()

prompt = connection.find_prompt()
print(prompt)

output = connection.send_command('show run')

mode = connection.check_config_mode()
print(mode)
if not mode:
    connection.config_mode()



print(output)

connection.disconnect()