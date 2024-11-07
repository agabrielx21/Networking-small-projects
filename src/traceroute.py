import socket
import traceback
import requests

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timeout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)

# Funcția pentru a obține informații despre locația unui IP
def get_location(ip):
    fake_HTTP_header = {
        'referer': 'https://ipinfo.io/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    # api_key = "7d4a4802625d58"  # înlocuiți cu cheia API corespunzătoare serviciului pe care îl utilizați
    url = f"https://ipinfo.io/widget/{ip}"
    response = requests.get(url, headers = fake_HTTP_header)
    data = response.json()
    return data

# Funcția pentru traceroute
def traceroute(ip, port = 443):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 64
    udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)

    # trimite un mesaj UDP catre un tuplu (IP, port)
    udp_send_sock.sendto(b'salut', (ip, port))

    # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
    # in cazul nostru nu verificăm tipul de mesaj ICMP
    # puteti verifica daca primul byte are valoarea Type == 11
    # https://tools.ietf.org/html/rfc792#page-5
    # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header
    addr = 'done!'
    try:
        data, addr = icmp_recv_socket.recvfrom(63535)
    except Exception as e:
        print("Socket timeout ", str(e))
        print(traceback.format_exc())
    return addr[0]  # returnam doar adresa IP a routerului

# Exemplu de utilizare pentru traceroute către adresa IP a unui site din China
ip_cn = "203.119.206.18"  # înlocuiți cu adresa IP a unui site din China
router_ip = traceroute(ip_cn)  # obținem adresa IP a routerului
print("Router IP:", router_ip)
ip_location_cn = get_location(router_ip)  # obținem informații despre locația routerului
print("China:")
print("City:", ip_location_cn["city"])
print("Region:", ip_location_cn["region"])
print("Country:", ip_location_cn["country"])

# Exemplu de utilizare pentru traceroute către adresa IP a unui site din Africa de Sud
# ip_za = "197.221.14.121"  # înlocuiți cu adresa IP a unui site din Africa de Sud
# ip_location_za = get_location(ip_za)
# print("Africa de Sud:")
# print("City:", ip_location_za["city"])
# print("Region:", ip_location_za["region"])
# print("Country:", ip_location_za["country"])

# Exemplu de utilizare pentru traceroute către adresa IP a unui site din Australia
# ip_au = "54.253.223.213"  # înlocuiți cu adresa IP a unui site din Australia
# ip_location_au = get_location(ip_au)
# print("Australia:")
# print("City:", ip_location_au["city"])
# print("Region:", ip_location_au["region"])
# print("Country:", ip_location_au["country"])
