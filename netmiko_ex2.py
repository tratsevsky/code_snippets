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

#entering the enable mode
connection.enable()

commands = ['int loop 1', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username user4 secret cisco']
connection.send_config_set(commands)

output = connection.send_command_expect('write memory')
print(output)


connection.disconnect()