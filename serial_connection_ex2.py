import serial
import time

def open_console(port='com3', baudrate=9600):
    console = serial.Serial(port, baudrate, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

def run_command(console, cmd='\n', sleep=1):
    print('Sending command: ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

def read_from_console(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        return False

con = open_console()
run_command(con)
run_command(con, 'show version')
output = read_from_console()
print(output)
