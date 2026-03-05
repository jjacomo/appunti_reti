# Iniziamo Reti

Trasmettitore ---------------------------> Ricevitore
                        canale

Tele = lontano => Telecomunicazione = comunicare lontano

Il problema principale e' quello dello spazio.
Portare una informazione lontano e velocemente non e' facile.
Le tecnologie di fine 700' sfruttavano tutte la luce (v = 299.792.548 m/s)
(btw nell'800 ci vuoleva circa 12 giorni per fare la traversata da EU a USA)

Episodio in cui muoiono 2500 inglesi in America anche se c'era gia' la pace 
perche' l'informazione non era ancora arrivata oltreoceano.
1865 primo cavo transatlantico telegrafico (impresa epica chiedilo a chatgpt)

## Canale

entità logica (lo stesso canale puo' essere implementato con diverse 
tecnologie fisiche) o fisica che permette il trasporto dei
singoli flussi informativi fra punti (nodi) remoti nello spazio

* Monodirezionale - l'informazione puo' essere trasferita in unica direzione
* Bidirezionale - l'informazione puo' essere trasferita in ambe le direzioni
* Punto-Punto - Un nodo e' collegato con un singolo nodo
* Punto-multipunto - Un nodo puo' comunicare con molti altri
    * Broadcast - tutti
    * Multicast - un sottoinsieme

## Rete

Due o più utenti utilizzano un mezzo fisico per
realizzare un canale per comunicare

Una grande popolazione di utenti vuole condividere un insieme di 
canali per comunicare a richiesta
- È necessario un sistema complesso che permetta il
“riuso” dei canali: la rete di telecomunicazioni

### Componenti della Rete

* `Terminali` ●
    - Fungono da interfaccia con l’utente finale
    - Codificano l’informazione in modo consono ad essere trasferita in rete
* `Collegamenti`  \
    - Permettono il trasferimento di uno o più flussi di informazione
    fra punti remoti nello spazio
* `Nodi di commutazione`  x
    - Utilizzano i mezzi trasmissivi al fine di creare canali
    di comunicazione sulla base degli richieste degli utenti


### Topologie di Rete

Descrizione geometrica di una rete

* Rami (`archi`)
    Linee di collegamento fra due nodi della rete
* `Nodi`
    Punti che si trovano agli estremi dei collegamenti
* La rete è descrivibile tramite un `grafo`

I grafi possono avere [maglie complete] se tutti i nodi sono connessi con gli altri
(richiedono un sacco di rami ma sono molto resilienti (anche se dei rami non vanno
possono comunicare lo stesso))
Dato che non sono molto viabili forse sono meglio le [maglie complete a stella] dove 
tutti i terminali sono collegati a un unico nodo di comunicazione che gli permette
di comunicare tra loro

.                                  rete di accesso
.                                        |
.                                        v
[rete gerarchica]: dove ci sono tanti terminali vicini metto una maglia completa a 
stella, quando esco da una rete "locale" e devo fare le distanze reali faccio piu'
maglie complete (nelle parti piu' centrali della rete).


## Collegamenti e Canali

I collegamenti sono realizzati con opportuni mezzi trasmissivi:
- Spazio libero (vuoto e aria)
- Cavi realizzati con materiali conduttori, principalmente rame
- Fibre ottiche in vetro e plastiche

Un collegamento e' fatto da un o PIU' canali.
Man mano che entro nella rete piu' centrale (non quella locale) i collegamenti 
diventano piu' thick (hanno piu' canali)

---

# Informazione, segnali, digitalizzazione

Le `sorgenti` di informazione possono essere grossolanamente classificate in tre categorie:
* Voce e suoni: utilizzati dall’orecchio umano
* Immagini: utilizzate dall’occhio umano
* Dati: tutto quello che non sia voce o immagini, normalmente rappresentato con 
        un qualche alfabeto convenzionale

Il problema delle telecomunicazioni moderne:
- Trasformare l’informazione originale prodotta dalla sorgente in un grandezza 
elettrica che rappresenta l’informazione
- Il risultato viene chiamato `segnale`

Ad esempio una sorgente sonora puo essere trasformata in un insieme di sinusoidi (fourier 
transform) e quindi tanti numeri di ampiezze e frequenze -> ecco i nostri numeri che poi
possiamo trasformare in segnali elettrici
<!-- E' la terza volta che dice sesso degli angeli -->
Attenzione i canali -banda passante- perdita di informazione (ad esempio le freq alte e
basse del telefono (ma va bene lo stesso))

---

20/02/2026 🟤 ﷼﷼﷼﷼﷼﷼﷼ ⛔

Le informazioni nel mondo fisico sono onde e quindi per andare al digitale:

* Conversione Analogico/Digitale (ADC)
    Il segnale analogico viene rappresentato in forma binaria, utilizzando le cifre 0,1 dette bit
    - Campionamento
    Il segnale analogico viene misurato in predeterminati istanti di tempo; Viene prodotta una serie temporali di numeri corrispondenti alle misure effettuate (se pero' campionassi alla stessa frequenza dell'onda sembrerebbe costante -> teorema di shannon-nyquist: campiona a 2 volte (almeno) la frequenza massima dell'onda)
    - Quantizzazione
    I numerici risultanti dal campionamento sono rappresentati in forma binaria utilizzando un numero di cifre predeterminato: piu' cifre uso maggiore e' la precisione e la fedelta' al segnale originale
* Conversione Digitale/Analogico (DAC)
    Una sequenza di bit viene riconvertita in una segnale analogico funzione del tempo


Nel mondo di oggi non ho piu' da pensare alle onde ma ai flussi di bit;
La rete risolve il problema di trasportare bit, non onde. 
E quindi un unica rete trasporta qualsiasi tipo di informazione perche' alla fine sono tutte trasformate in bit.
La riconversione dall'altro verso viene fatta dal tuo computer una volta che i bit arrivano al tuo computer.


## ITU: tassonomia dei servizi

* Servizi `interattivi`: esiste interazione fra sorgente e destinazione
    - [Conversazione]
        Scambio informativo in tempo reale: telefonia, condivisione di file system
    - [Messaggistica]
        Scambio informativo in tempo differito con memorizzazione: posta elettronica, SMS
    - [Consultazione]
    Scambio informativo con flusso controllato dall’utente: WWW, teledidattica
* Servizi `distributivi`: la sorgente diffonde informazioni in modo indipendente ad un numero imprecisato di destinazioni
    - [Senza controllo di presentazione]
        L’utente di destinazione non controlla l’ordine con cui ricevere le informazione: radio/tele-diffusione
    - [Con controllo di presentazione]
        L’utente di destinazione può controllare l’ordine con cui ricevere le informazione: televideo

E poi si dividono in
* Servizio monomediale
    - Trasporta informazioni di un solo tipo
    - Trasferisce più tipologie di informazione sotto forma di un solo segnale
        * Televisione: immagine e suoni in un unico segnale analogico opportunamente costruito
* Servizio multimediale
    - Trasporta informazioni di almeno due tipologie diverse
    - Le diverse tipologie di informazioni sono trasportate dalla medesima rete ma con modalità distinte
        * Diversi protocolli
        * Differenti qualità di servizio (conformi alla tipologia di informazione)
            * Videoconferenza: voce e video bidirezionale

### Qualita' dei servizi

nelle slide:
Jitter - quanto i ritardi sono variabili

---

# 26/02/2026

## Compensazione al terminale 

(slide 88)

visto che i dati nella rete possono essere ritardati un po' varialmente quindi prima di fare vedere un video invece di mandare i dati appena arrivo li metti in un buffer

## Multiplazione (Multiplexing)

Come trasferire piu' informazioni (flussi di bit che codificano per cose diverse) sullo STESSO CANALE.
Canale = cosa logica che collega due nodi (tipo aria)
COllegamento = come comunicare sul canale (tipo parlando)

.               diverse sorgenti
                       |
                       V
Per Multiplexare flussi di bit su un canale li devo trasmettere a `TEMPI` diversi (ovviamente non ha senso sovrapporre bit tra di loro o altro) -> `TDM` (Time Division Multiplexing)
(ad esempio ci sarebbe anche la FDM (frequency - tipo le radio che trasmettono su frequenze diverse))

* TDM `Slotted`:
    * `Framed`
    * `UnFramed`
* TDM `UnSlotted`:

<!-- Paese di Bengodi = Paradiso terrestre immaginario, pieno d’ogni ben di Dio. -->

Oggin abbiamo [unslotted e dinamica] e [slotted e statica]

RIpassa tutto, abbiamo finito il primo pdf
Commutazione

