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
La correzione costa: 1000bit (rimando tutto il pacchetto)

### correzione
Faccio che assieme ai 1000bit del pacchetto ne aggiungo 10 (che bastano) per correggere gli altri
Se c'e' un pacchetto sbagliato quindi lo posso correggere.
La rilevazione costa: 10bit
La correzione costa: 10

Se e' molto probabile fare errori allora conviene la correzione.
Altrimenti la rivelazione.


# 12/03/2026

## Codici a blocco

Blocco = k bit
Codice (di rilevazione errore) = r bit
n = k + r  <-- sarebbe il pacchetto lungo n (PCI + SDU)
Tutti questi numeri sono prestabiliti cosi' che chi riceve sa come risuddividere il messaggio

## Codici sistematici

Nella sequenza di n bit da trasmettere i k bit di informazione, mantenuti distinti dagli r bit di ridondanza, vengono trasmessi inalterati

![Errore in ricezione](./errRicezione.png)

Partiamo dal presupposto che i k sono tanti rispetto agli r.
Quindi se r e k differiscono do' la colpa ai k bit (probabilmente l'errore e' avvenuto li') e mi faccio ristrasferire tutto (anche se in teoria potrebbero essere giusti ma sbagliato r).

## che codifica usare?

### Bit di Parita'

Conta i bit a 1. Metti r (1bit) a 0 o 1 in modo da fare venire il totale degli 1 un numero pari.
In pratica questo si fa con mettendo a XOR tutti i bit k.
Quindi e' velocissimo!

Ma e' funziona?
Si solo se sbagli un numero dispari di bit.
Quindi lo puoi usare solo se k e' abbastanza piccolo (ad esempio nella prima versione ascii l'ottavo bit e' usato per la correzione.

### Checksum

Quello che si usa oggi.
Si puo' calcolare per un numero qualsiasi di blocchi (multiplo di 16, se non lo e' si fa un po' di padding).
Si dividono i bit in blocchi da 16.
Si fa la somma complemento a 1 di tutti i blocchi.
Quando ho un bit carry lo sommo come bit meno significativo.
Poi metto questo numero nel PCI.

In ricezione basta fare la somma di tutti i blocchi come prima sommando anche il numero checksum del PCI.
Se il risultato viene con tutti i bit a 1 il messaggio e' giusto!!!!

Funziona benissimo per rilevare gli errori, il suo difetto e' che devi usare 16 bit (che non sono pochissimi).
Quindi se hai pacchetti formati da poche parole (blocchi) non e' molto consigliato usare il checksum.

Funziona sia bigEndian che littleEndian (ovviamente) (si puo' usare anche su architetture diverse).
<!-- sesso degli angeli counter +1 -->
### Codici polinomiali

[A / B = Q + r]

Fisso B (protocollo fissato).
Trasmetto A solo multipli di B.
Se A arriva sbagliato non e' piu' divisibile per B (da resto) e allora me ne accorgo.

La cosa bella e' che in binario fare somme e' uguale a fare sottrazioni.
Questo e' il principio, vediamo come funziona:

* Trasformo sequenze di bit in polinomi
    10010 = x^4 * 1 + x^3 * 0 + x^2 * 0 + x * 1 + 1 * 0 = P(x)
* Divisione tra polinomi:
    [P(x) / G(x) = Q(x) + r(x)]  <-- G(x) e' concordato (protocollo)
    Ricorda la divisione in colonna (si fa con le sottrazioni => in binario e' velocissimo)
    Bisogna scegliere furbescamente G(x) in modo da (?) . 
    G(x) e' dello stesso grado di P(x) => nel mondo binario viene fuori sempre un polinomio di grado minore



