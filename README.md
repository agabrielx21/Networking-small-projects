- Traceroute
  Traceroute este o metodă prin care putem urmări prin ce noduri (routere) trece un pachet pentru a ajunge la destinație. În funcție de IP-urile acestor noduri, putem afla țările sau regiunile prin care trec pachetele. Înainte de a implementa tema, citiți explicația felului în care funcționează traceroute prin UDP. Pe scurt, pentru fiecare mesaj UDP care este în tranzit către destinație, dar pentru care TTL (Time to Live) expiră, senderul primește de la router un mesaj ICMP de tipul Time Exceeded TTL expired in transit.
