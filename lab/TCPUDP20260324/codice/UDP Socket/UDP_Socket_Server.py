'''
                            UDP SERVER SOCKET
Corso di Programmazione di Reti - Laboratorio - Università di Bologna
G.Pau - A. Piroddi
'''

import socket as sk
import time

# Creiamo il socket
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# associamo il socket alla porta
server_address = ('localhost', 10000) # 127.0.0.1
# ma se invece ci mettessi l'ip della mia interfaccia ethernet ? provaci (dopo dovrai entrarci da un altro dispositivo).
print ('\n\r starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print('\n\r waiting to receive message...')
    data, address = sock.recvfrom(4096) # quidni e' bloccante (?)

    print('received %s bytes from %s' % (len(data), address))
    print (data.decode('utf8'))
    
    
    if data:
        data1='Programmazione di Reti'
        time.sleep(2)
        sent = sock.sendto(data1.encode(), address)
        print ('sent %s bytes back to %s' % (sent, address))

