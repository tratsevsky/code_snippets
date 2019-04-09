from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()

# list all available methods
print(dir(ios))

ios.close()