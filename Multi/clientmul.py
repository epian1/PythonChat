import socket
import thread
import sys

pin ='ABC'

def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data
	
def recv_data():            #Receive data from other clients connected to server
    while 1:
        try:
            recv_data = client_socket.recv(4096)            
        except:
            #Process terminates
            print "Server closed connection"
            thread.interrupt_main()     # Interrupt main wen socket closes
            break
        if not recv_data:               # If recv has no data, close conection (error)
                print "Server closed connection"
                thread.interrupt_main()
                break
        else:
            print "\nReceived data: ", recv_data
            recv_data = xor(recv_data, pin)
            print "Dectrypted data: ", recv_data

def send_data():                # Send data from client to server"
    while 1:
        send_data = str(raw_input(">> (q to quit):\n"))
        if send_data == "q" or send_data == "Q":
            client_socket.send(send_data)
            thread.interrupt_main()
            break
        else:
            send_data = xor(send_data, pin)
            client_socket.send(send_data)
        
if __name__ == "__main__":

    print "||||| TCP Client ||||"
    ip = str(raw_input("Enter server IP to connect: "))
    print "Connecting to ",ip,":6666"
    
    user = str(raw_input("Enter username:"))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 6666))

    print "Connected to ", ip,":6666"
    #usr = str(raw_input("Enter username: ")

    thread.start_new_thread(recv_data,())
    thread.start_new_thread(send_data,())

    try:
        while 1:
            continue
    except:
        print "Client program quits...."
        client_socket.close()       
