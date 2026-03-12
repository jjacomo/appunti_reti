# Modello ISO/OSI

Non vogliamo sistemi chiusi (propietari). Crea incompatibilita' e rotture di coglioni per i consumatori

L'OSI a una certa dice usiamo degli STANDARD.
Come fare parlare due calcolatori insieme quindi? Beh non in una botta sola:
In layers, dividere il problemi in 7 sottoproblemi.

Questi 7 layers comunicano tra di loro grazie a `interfacce`.
Ognuno fa la propria parte (nessuno deve fare tutto altrimenti e' folle)

I `Protocolli` fanno comunicare due layers dello stesso livello remoti

## Come comunicano tra di loro layer dello stesso livello (protocolli)

Aggiungendo man mano delle etichette ai dati e passandolo al layer dopo

N-`Protocol Control Information` (PCI): informazioni aggiuntive per il controllo del dialogo a livello N
Quando scendi gli strati vengono aggiunte. Fino a quando si arriva al filo fisico.
Quando arriva all'altro computer si risale spacchettando man mano le etichette.

N-`Protocol Data Unit` = dati trasferiti fra entità di strato N
Quindi il PDU scendendo gli strati si ingrandisce aggiungendo PCI (al SDU = Service Data Unit (il payload))


DI questi 7 layer due sono fondamentali.
il 3 e il 4. Perche' sono quelli che interfacciano le reti fisiche ai calcolatori (????)

Anyways bisogna che questi 2 siano identici tra tutti (stesso codice in tutti i sistemi operativi)

## Oggi c'e' TCP/IP non OSI

OSI 7, 6, 5   <->     TCP/IP  4 (applicazione) (HTTP, TELNET, SMTP, DNS, ...)
OSI 4         <->     TCP/IP  3 (trasporto) (TCP, UDP)
OSI 3         <->     TCP/IP  2 (network) (IP, ICMP, ARP, ...)
OSI 2, 1      <->     TCP/IP  1 (link) (ETHERNET, IEEE802, ..)

Il codice TCP/IP e' Stato rilasciato nell'83 PUBBLICAMENTE (una roba inaudita per quel tempo) e qualcuno lo infila in UNIX e da allora e' esploso l'utilizzo di TCP/IP


## Come indirizzare?

Come faccio a mandare i messaggi a un computer specifico della rete che scelgo io?

Tipicamente dobbiamo distinguere fra
- Identifier
    Identificativo di una certa risorsa di rete
- Locator
    Indirizzo necessario per localizzare tale risorsa

In Internet:
- Uniform Resource Name o URN
- Uniform Resource Identifier o URI
- Uniform resource locator o URL: identifica una risorsa 

Indirizzo `globale`
- È valido per tutta la rete
- Deve essere univoco (non devono esistere indirizzi replicati) per evitare ambiguità
- Va “assegnato” seguendo una procedura di gestione “globale” che assicura la non replicazione
Indirizzo `locale`
- È valido limitatamente ad un certa sottoporzione della rete
    * Internamente ad un terminale
    * In un dominio di rete specifico
- Può non essere univoco
- Può essere assegnato con una procedura puramente “locale



ad esempio il [MAC] e' globale. Sarebbe fisso ma in realta' si puo' cambiare (PERICOLO SPOOFING).
Serve per fare l'indirizzameto sul livello fisico.
Serve per aiutare i nostri dispositvi a capire quali dati sono per loro.
Se ogni computer dovesse leggere i dati che passano sulla rete (che sono per un sacco di gente e sono tantissimi) sprecherebbe un sacco di tempo.

Indirizzo [IP]: 4 byte (IPv4). E' un Locator GLOBALE. E' come il tuo indirizzo.

Numero di [Porta]: valore a 16 bit rappresentato come numero da 0 a 65535 e dice una volta che e' arrivato al computer il messaggio a che applicazione darlo. Se l'ip e' l'indirizzo, il numero di porta e' il numero dell'appartamento.

IP + Porta = Endpoint

`Well Known Ports`: alcune applicazioni hanno porte predefinite: HTTP: 80; SSH: 22; ...

`DNS`: traduce parole intelleggibili da umani in IP


# 05/03/2026

Per identificare il singolo flusso è sufficiente
conoscere:
- IP sorgente
- IP destinazione
- Porta sorgente
- Porta destinazione

"Per poter chiamare qualcuno quel qualcuno deve stare attento a rispondere" =>

## Server

Con il termine `server` indichiamo un’[applicazione] che:
- rende disponibile un servizio
- mediante un’interfaccia standard (protocollo)

Il processo Server si predispone a ricevere una connessione eseguendo una `apertura passiva`
- Si mette in ascolto in attesa dell’arrivo di una richiesta di connessione
    Questo processo nel mondo Unix è chiamato `Demone` (Daemon)

Quindi un server non e' un propriamente un computer.
Quando un computer ha molte applicazioni server allora nel linguaggio comune si dice che e' un server.
Ma server e' riferito alle applicazioni non ai computer.

## Client

Con il termine `client` indichiamo un’[applicazione] che:
- È in grado di utilizzare i servizi messi a disposizione da un server.

Il processo Client esegue una apertura attiva
- Tenta di collegarsi al processo server di destinazione (suppone che esista)


# Come faccio a sapere l'ip dei server? (e numero di porta)

"Come faccio a conoscere il numero di telefono".
Fortunatamente non si usano piu' i mega elenchi telefonici

## Per le porte

Come gia' detto prima:
La IANA ha diviso i numeri di porta in 3 gruppi:
* `well known ports`: non dovresti creare applicazioni che usano queste porte (senza l'autorizzazione di IANA) sono dall'1 al 1023. (All'inizio arrivavano solo a 255)
* `Registrate`: da 1024 a 49151. Sono usari da alcuni servizi ma anche da client.
* `ad uso dei client`: da 49151 a 65535

Questo e' per i server. 
Per i client e' tutto piu' rilassato: infatti quando un client manda un messaggio a un server manda anche il numero di porta dell'applicazione dove vuole la risposta, quindi non c'e' bisogno che i server sappiano a priori questa porta.


## DNS

* Affinchè un calcolatore possa parlare con altri calcolatori su Internet:
    - DEVE essere equipaggiato con almeno una interfaccia di rete
    - L’interfaccia di rete DEVE avere associato un numero IP
* Al calcolatore PUO’ essere associato un nome simbolico
    - Sequenza di stringhe alfanumeriche separate da punti deisnet.deis.unibo.it
* Perché un nome simbolico? Per renderlo più facilmente fruibile agli essere umani

Ogni calcolatore quindi ha un nome specifico associato al suo ip

Vai alla prossima cartella






















