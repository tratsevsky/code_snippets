from netmiko import ConnectHandler

# Import config for multiple devices
with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'u1',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose': True
    }
    device_list.append(cisco_device)

# print the first item if necessary
# print(device_list[0]['ip'])

for device in device_list:
    print('Connecting to ' + device['ip'])
    connection = ConnectHandler(**device)
    #entering the enable mode
    connection.enable()

    file = input('Enter configuration file (use a valid path) for ' + device['ip'] + ':')

    print('Running commands from file:', file, 'to device', device['ip'])
    output = connection.send_config_from_file(file)
    print(output)

    connection.disconnect()