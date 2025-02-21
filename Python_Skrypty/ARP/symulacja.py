import time

arp_table = {
    "192.168.1.1": "00:1A:2B:3C:4D:5E", 
    "192.168.1.10": "AA:BB:CC:DD:EE:FF", 
}

def send_arp_request(ip_address):
    """Symulacja ARP Request"""
    print(f"[ARP REQUEST] Kto ma adres IP {ip_address}? Podaj mi swój MAC!")
    time.sleep(1)  
    return arp_reply(ip_address)

def arp_reply(ip_address):
    """Symulacja ARP Reply"""
    if ip_address in arp_table:
        mac_address = arp_table[ip_address]
        print(f"[ARP REPLY] IP {ip_address} ma MAC {mac_address}")
        return mac_address
    else:
        print(f"[ARP REPLY] Brak odpowiedzi - nie znaleziono IP {ip_address}")
        return None

def update_arp_cache(ip, mac):
    """Aktualizacja lokalnej tablicy ARP"""
    print(f"[CACHE UPDATE] Dodano: {ip} -> {mac}")
    arp_table[ip] = mac

target_ip = "192.168.1.10"
print(f"[SYSTEM] Wysyłam pakiet do {target_ip}, ale nie znam MAC...")

resolved_mac = send_arp_request(target_ip)

if resolved_mac:
    update_arp_cache(target_ip, resolved_mac)

print("\n[AKTUALNA TABLICA ARP]")
for ip, mac in arp_table.items():
    print(f"{ip} -> {mac}")
