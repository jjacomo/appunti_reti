# Corso di Programmazione di Reti - Laboratorio - Universita'  di Bologna
# Socket_Programming_Assignment - WebServer - F. Callegati - G.Pau - A. Piroddi

import sys
from socket import * # libreria socket per fare i socket :)
serverPort=8080 # In che porta ascolta il server web? 8080
serverSocket = socket(AF_INET, SOCK_STREAM) # ricorda AF_INET che cos'e' (?) # SOCK_STREAM perche' si parlano a vicenda (?) (l'UDP e' per applicazioni real-time (meno controlli, piu' veloci)
server_address=('localhost',serverPort)
serverSocket.bind(server_address) # binda l'indirizzo IP e la port ==> ora e' un socket vero e proprio!!!

#listen(1) Definisce la lunghezza della coda di backlog, ovvero il numero
#di connessioni in entrata che sono state completate dallo stack TCP / IP
#ma non ancora accettate dall'applicazione.
serverSocket.listen(1) # il server si mette ad ascoltare le richieste. E' una istruzione bloccante, finche' non gli arriva una richiesta non fa niente.
print ('the web server is up on port:',serverPort)

while True:

    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket,addr)

    try:

        message = connectionSocket.recv(1024)
        if len(message.split())>0:
            print (message,'::',message.split()[0],':',message.split()[1])
            filename = message.split()[1]
            print (filename,'||',filename[1:])
            f = open(filename[1:],'r+')
            outputdata = f.read()
            print (outputdata)
                
     #Invia la riga di intestazione HTTP nel socket con il messaggio OK

            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            

    except IOError:
 #Invia messaggio di risposta per file non trovato
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n","UTF-8"))
        connectionSocket.close()

# BTW 
# L'indirizzo di loopback e' 127.0.0.1
# fai partire questo file e metti sul browser http://127.0.0.1:8080/index.html
