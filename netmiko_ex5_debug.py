from netmiko import ConnectHandler
# Netmiko debug: option 1 (by kbuyers)
import logging
logging.basicConfig(filename='logg.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
# end of option 1
from time import sleep


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
connection.enable()

connection.write_channel('show run\n')
time.sleep(3)

connection.disconnect()