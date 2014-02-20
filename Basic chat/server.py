import socket                       # Import socket module
import operator                     # For encypt.
import sys

pin = 'ABC'                         # Encryption pin

sucket = socket.socket()            # Socket object
host = socket.gethostname()         # Get host name
port = 9999                         # Reserve best port.
 
 
print 'Server started'
print 'Waiting for cients to connect...'
 
sucket.bind((host, port))           # Bind to the port
sucket.listen(3)                    # Now wait for client connection.
c, addr = sucket.accept()           # Establish connection with client.
print 'Got connection from', addr

################### Encryption ###############################
def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data

################### Chat implementation #######################

while True:
   msg = c.recv(1024)
   msg = xor(msg, pin)

   print '\n', addr, 'Decrypted : ', msg
   msg = raw_input('\n|| Server || : ')
   msg = xor(msg, pin)
   print 'Encrypted :', msg
   c.send(msg);
   #c.close()                       # Close the connection
