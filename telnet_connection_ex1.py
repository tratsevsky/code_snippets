import telnetlib
import getpass

host = '10.1.1.1'
user = 'cisco'
# password = 'cisco'
password = getpass.getpass() # getpass works only when script is run in console (outside IDE)

tn = telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(user.encode() + b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n') #this is an enable password
tn.write(b'terminal length 0\n')
tn.write(b'show run\n')
tn.write(b'exit\n') #important to terminate session because read won't success w/o it

result = tn.read_all().decode()
print(result)