from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()

# list all available methods
# print(dir(ios))

# output = ios.get_facts()
# output = ios.get_interfaces()
output = ios.ping(destination='10.1.1.22', count=2)

dump = json.dumps(output, sort_keys=True, indent=2)
print(dump)

ios.close()