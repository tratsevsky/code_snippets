class Device:
    def __init__(self, ip, username, password, connection=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.connection = connection

    def connect(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ip)

    def authenticate(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.username.encode() + b'\n')
        self.connection.read_until(b'UPassword: ')
        self.connection.write(self.password.encode() + b'\n')

    def send(self, command):
        self.connection.write(command.encode() + b'\n')

    def show(self):
        output = self.connection.read_all().decode('utf-8')
        return output

with open('devices.txt', 'r') as f:
    device = f.read().splitlines()

ip = list()
for item in device:
    tmp = item.split(':')
    ip.append(tuple(tmp))

for element in ip:
    router1 = Device(element[0], 'user', 'pass')
    router1.connect()
    router1.authenticate()
    router1.send('enable')
    router1.send('cisco') #this is the enable password
    router1.send('term len 0')
    router1.send('conf t')
    router1.send('inerface lo0')
    router1.send('ip address ' + str(element[1]) +' 255.255.255.255')
    router1.send('exit')
    router1.send('router ospf 1')
    router1.send('network 0.0.0.0 0.0.0.0 area 0')
    router1.send('end')
    router1.send('show ip protocols')

    output = router1.show()
    print(output)
