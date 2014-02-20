import socket                   # Import socket module
import operator
import sys

pin = 'ABC'

sucket = socket.socket()            # Socket object
host = socket.gethostname()         # Get host name
port = 9999                         # Reserve best port.
 
print 'Connect to ', host, port
sucket.connect((host, port))

################# Here the connection protocol is done ###################
def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data

################# Enctryption ####################################### 
while True:
    msg = raw_input('\n|| Cient || : ')
    msg = xor(msg, pin)
    print 'Encrypted: ', msg
    sucket.send(msg)

    msg = sucket.recv(1024)
    msg = xor(msg, pin)
    print '\nDecrypted'
    print '|| Server || : ', msg
#s.close                     # C
