In una rete e' molto comune che i pacchetti arrivino in ordine abbastanza sparso.
Non e' detto che se parti prima arrivi prima (dipende che strada fai sulla rete)

Come si fa a garantire 
# Errori di trasmissione

* Codifica di canale con codici a rivelazione di errore
* Conferma di ricezione e ritrasmissione

Devo capire come capire se i bit sono sbagliati. Lo faccio attraverso una [codifica di canale].

Ad esempio potrei inventarmi una codifica per cui ogni bit della codifica di sorgente lo mando 2 volte.
Quindi se voglio mandare 1001 mando 11000011 in questo modo e ricevo dei bit sballati lo trovo subito.
Ovviamente se vengono sballati entrambi non ci posso fare nulla ma e' poco probabile.
<!-- spiderman ha calpestato il banco proprio difronte a callegati INCREDIBILE era proprio li' di fronte ma e' come se callegati abbia fatto finta di niente. -->
<!-- ha usato l'espressione "conti della serva" -->
Esistono codici solo per capire se ci sono errori e altri per correggerli invece (che capiscono anche se ci sono)

## codici di rivelazione o correzione errore

Voglio che i dati arrivino tutti giusti.

### rivelazione
In un pacchetto di 1000 bit ne basta anche 1 solo per capire se e' sbagliato.
Facciamo che se trovo un bit sbagliato mi faccio rimandare il pacchetto sbagliato.
La rilevazione costa: 1bit
La correzione costa: 1000bit (tutto il pacchetto)

### correzione
Faccio che assieme ai 1000bit del pacchetto ne aggiungo 10 (che bastano) per correggere gli altri
Se c'e' un pacchetto sbagliato quindi lo posso correggere.
La rilevazione costa: 10bit
La correzione costa: 10 (tutto il pacchetto)

Se e' molto probabile fare errori allora conviene la correzione.
Altrimenti la rivelazione.

