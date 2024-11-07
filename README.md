## Traceroute
  Traceroute este o metodă prin care putem urmări prin ce noduri (routere) trece un pachet pentru a ajunge la destinație. În funcție de IP-urile acestor noduri, putem afla țările sau regiunile prin care trec pachetele. Înainte de a implementa tema, citiți explicația felului în care funcționează traceroute prin UDP. Pe scurt, pentru fiecare mesaj UDP care este în tranzit către destinație, dar pentru care TTL (Time to Live) expiră, senderul primește de la router un mesaj ICMP de tipul Time Exceeded TTL expired in transit.

## Server DNS Add Blocker

## ARP Spoofing (2p)
ARP spoofing presupune trimiterea unui pachet ARP de tip reply către o țintă pentru a o informa greșit cu privire la adresa MAC pereche pentru un IP.

Arhitectura containerelor este definită aici, împreună cu schema prin care `middle` îi informează pe `server` și pe `router` cu privire la locația fizică (adresa MAC) unde se găsesc IP-urile celorlalți. 


```
            MIDDLE------------\
        subnet2: 198.7.0.3     \
        MAC: 02:42:c6:0a:00:02  \
               forwarding        \ 
              /                   \
             /                     \
Poison ARP 198.7.0.1 is-at         Poison ARP 198.7.0.2 is-at 
           02:42:c6:0a:00:02         |         02:42:c6:0a:00:02
           /                         |
          /                          |
         /                           |
        /                            |
    SERVER <---------------------> ROUTER <---------------------> CLIENT
net2: 198.7.0.2                      |                           net1: 172.7.0.2
MAC: 02:42:c6:0a:00:03               |                            MAC eth0: 02:42:ac:0a:00:02
                           subnet1:  172.7.0.1
                           MAC eth0: 02:42:ac:0a:00:01
                           subnet2:  198.7.0.1
                           MAC eth1: 02:42:c6:0a:00:01
                           subnet1 <------> subnet2
                                 forwarding
```
