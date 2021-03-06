from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()

# list all available methods
# print(dir(ios))

output = ios.get_arp_table()
# print(type(output))
# for item in output:
#     print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
with open('arp.txt', 'w') as f:
    f.write(dump)

ios.close()