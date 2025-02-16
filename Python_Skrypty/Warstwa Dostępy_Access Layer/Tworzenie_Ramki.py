import time
import sys

def animate_frame_creation():
    frames = [
        "[                      ]",  # Pusta ramka
        "[MAC-DST: 3C:97:0E:67:89:AB]",  # Adres docelowy
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E]",  # Adres źródłowy
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800]",  # Typ ramki (IPv4)
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800 | IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5]",  # Adresy IP
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800 | IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5 | TCP-SRC: 443 | TCP-DST: 56789]",  # Porty TCP
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800 | IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5 | TCP-SRC: 443 | TCP-DST: 56789 | SEQ: 1001 | ACK: 2001 | FLAGS: SYN,ACK]",  # TCP handshake
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800 | IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5 | TCP-SRC: 443 | TCP-DST: 56789 | SEQ: 1002 | ACK: 2002 | FLAGS: PSH,ACK | DATA: HTTP GET]",  # Dane
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E | TYPE: 0x0800 | IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5 | TCP-SRC: 443 | TCP-DST: 56789 | SEQ: 1002 | ACK: 2002 | FLAGS: PSH,ACK | DATA: HTTP GET | FCS: 0xA1B2C3D4]",  # Suma kontrolna
    ]
    
    print("Tworzenie pakietu Ethernet z TCP:")
    for frame in frames:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\nPakiet został wysłany!\n")

def animate_network_transfer():
    frames = [
        "[Host: Wysyłanie pakietu]",
        "[Switch: Odbiór ramki | Odczyt MAC | Przekazanie do routera]",
        "[Router: Odbiór pakietu | Odczyt IP | Routing]",
        "[Router: Przekazanie pakietu do sieci docelowej]",
        "[Switch: Odbiór ramki | Przekazanie do hosta docelowego]",
        "[Host docelowy: Odbiór pakietu | Dekapsulacja | Przetwarzanie danych]",
    ]
    
    details = [
        "[MAC-DST: 3C:97:0E:67:89:AB | MAC-SRC: 00:1A:2B:3C:4D:5E]",
        "[IP-SRC: 192.168.1.10 | IP-DST: 10.0.0.5]",
        "[Router: Odczyt IP 10.0.0.5 | Wyszukiwanie trasy]",
        "[Router: Przekazanie pakietu przez interfejs WAN | Nowy MAC-DST: 58:BF:EA:12:34:56 | MAC-SRC: 3C:97:0E:67:89:AB]",
        "[Switch: Odbiór ramki | MAC-DST: 58:BF:EA:12:34:56 | MAC-SRC: 3C:97:0E:67:89:AB | Przekazanie do hosta]",
        "[Host docelowy: Dekapsulacja | TCP SEQ: 1002 | ACK: 2002 | HTTP GET | Przetwarzanie danych]",
    ]
    
    print("Symulacja komunikacji między hostem, switchem i routerem:")
    for i in range(len(frames)):
        sys.stdout.write("\r" + frames[i])
        sys.stdout.flush()
        time.sleep(1)
        print("\n" + details[i])
    
    print("\nDane dotarły do hosta docelowego i zostały przetworzone!")

def animate_decapsulation():
    steps = [
        "[Host docelowy: Otrzymano ramkę Ethernet]",
        "[Usuwanie nagłówka Ethernet | Sprawdzanie MAC]",
        "[Usuwanie nagłówka IP | Sprawdzanie adresu IP]",
        "[Usuwanie nagłówka TCP | Sprawdzanie portów]",
        "[Odczyt danych: HTTP GET]",
        "[Dane gotowe do przetworzenia przez aplikację]",
    ]
    
    print("\nProces dekapsulacji na hoście docelowym:")
    for step in steps:
        sys.stdout.write("\r" + step)
        sys.stdout.flush()
        time.sleep(1)
        print("\n")
    
    print("\nKomunikat HTTP został przekazany do aplikacji!")

if __name__ == "__main__":
    animate_frame_creation()
    animate_network_transfer()
    animate_decapsulation()