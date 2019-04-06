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

# run commands from file (full filepath is also supported)
connection.send_config_from_file('ospf.txt')

connection.disconnect()