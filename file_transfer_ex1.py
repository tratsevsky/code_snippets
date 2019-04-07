from netmiko import ConnectHandler
from netmiko import file_transfer # SCP support

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection, source_file='ospf.txt', dest_file='ospf1.txt',
                                file_system='disk0:', direction='put', overwrite_file=True)

print(transfer_output)
