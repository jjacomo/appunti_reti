# DNS in lab

Il server DNS usa la porta (well known) 53.
Porta + IP = [socket]

Traduce nomi letterali in IP:
_plus.google.com_  ==>  216.58.209.46


L'applicazione che cerca google chiede al sistema operativo e, se ha quel nome,
(c'e' una cache (`resolver`) dove si salvano un po' di nomi frequenti) te lo rida' subito.
Se il resolver del sistema non ti da niente allora si va a chiedere al router.
Al router chiede a sua volta se ha il nome nella sua cache (`secondo resolver`).
Se, a sua volta non lo sa, il router va al `Root Server`.
Il Root Server non ha direttamente l'ip del nome ma ti dice a che server chidere guardando il top level domain (.com; .net; .it; ....).


Per vedere che resolver stai usando fai

```bash
cat /etc/resolv.conf
```
Con wireshark controlla che il pacchetto del dns abbia l'ip che hai visto qui

Per vedere la cache dns del tuo sistema

```bash
systemd-resolve --statistics
```


### Wireshark

E' un analizzatore di protocollo.
All'inizio devi selezionare l'interfaccia di rete che vuoi analizzare.
Scheda di rete? Ethernet? Altro? ...
Vedi tutte le interfacce facendo 
```bash
ip addr
```

La scheda di rete ha la funzione di scartare tutti i pacchetti che non sono indirizzati a lei (non hanno il tuo mac/ip addr)
Pero' si puo' mettere la scheda di rete in modalita' promisqua e guardare anche gli altri.

## Oltre all'ip

Il DNS non ti dice solo l'IPv4.
Ti dice anche l'IPv6.
Ti dice anche il record MX. Quando configuri l'email ti viene dato anche un tuo mail server (?)
Ti dice anche il PTR che serve a fare la query inversa (come si chiama 123.345.32.129 ?) (in_addr.arpa e' il server che fa sta roba (?))

### Comando traceroute

```bash
traceroute www.sitoacaso.com
```













