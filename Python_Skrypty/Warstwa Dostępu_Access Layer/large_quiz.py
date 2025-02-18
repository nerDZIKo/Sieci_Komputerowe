import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def quiz():
    questions = [
        {"question": "Które dwie warstwy modelu OSI mają taką samą funkcjonalność jak dwie warstwy modelu TCP/IP?",
         "options": ["sieć", "sesja", "łącze danych", "fizyczny", "transport"],
         "correct": ["łącze danych", "fizyczny"]},

        {"question": "Które trzy akronimy reprezentują organizacje normalizacyjne?",
         "options": ["IEEE", "IETF", "OSI", "IANA", "TCP/IP", "MAC"],
         "correct": ["IEEE", "IETF", "IANA"]},

        {"question": "Jakie trzy elementy mają wspólne wszystkie metody komunikacji?",
         "options": ["medium transmisyjne", "typ wiadomości", "priorytet wiadomości", "miejsce docelowe wiadomości", "źródło wiadomości", "dane wiadomości"],
         "correct": ["medium transmisyjne", "miejsce docelowe wiadomości", "źródło wiadomości"]},

        {"question": "Które trzy warstwy mapy modelu OSI do warstwy aplikacji modelu TCP/IP?",
         "options": ["aplikacja", "łącze danych", "sieć", "transport", "prezentacja", "sesja"],
         "correct": ["aplikacja", "prezentacja", "sesja"]},

        {"question": "Która instrukcja definiuje protokół komunikacji danych?",
         "options": ["Zestaw standardów produktów", "Umowa wymiany danych", "Sojusz producentów", "Zestaw zasad komunikacji"],
         "correct": "Zestaw zasad komunikacji"},

        {"question": "Który protokół służy do dynamicznego przydzielania adresów IP?",
         "options": ["DNS", "HTTP", "DHCP", "FTP"],
         "correct": "DHCP"},

        {"question": "Jaki jest główny cel NAT?",
         "options": ["Zarządzanie ruchem", "Ukrywanie adresów IP", "Szyfrowanie", "Poprawa QoS"],
         "correct": "Ukrywanie adresów IP"},

        {"question": "W jakiej warstwie modelu OSI działa switch?",
         "options": ["Fizyczna", "Łącza danych", "Sieciowa", "Transportowa"],
         "correct": "Łącza danych"},

        {"question": "Jakie są główne zadania warstwy transportowej?",
         "options": ["Adresacja IP", "Zarządzanie sesją", "Kontrola przepływu", "Routing"],
         "correct": "Kontrola przepływu"},

        {"question": "Jaki protokół jest używany do bezpiecznego przesyłania stron WWW?",
         "options": ["HTTP", "FTP", "HTTPS", "SNMP"],
         "correct": "HTTPS"},

        {"question": "Który adres IPv4 jest adresem rozgłoszeniowym?",
         "options": ["192.168.1.255", "192.168.1.1", "127.0.0.1", "255.255.255.0"],
         "correct": "192.168.1.255"},

        {"question": "Jaką długość ma standardowy adres IPv6?",
         "options": ["32 bity", "64 bity", "128 bitów", "256 bitów"],
         "correct": "128 bitów"},

        {"question": "Jak nazywa się proces wykrywania adresów MAC przez switch?",
         "options": ["Routing", "Flooding", "MAC learning", "ARP discovery"],
         "correct": "MAC learning"},

        {"question": "Co robi router, gdy nie zna adresu docelowego?",
         "options": ["Usuwa pakiet", "Przekazuje losowo", "Odrzuca pakiet", "Wysyła do bramy"],
         "correct": "Wysyła do bramy"},

        {"question": "Który protokół jest używany do przesyłania e-maili?",
         "options": ["IMAP", "POP3", "SMTP", "DNS"],
         "correct": "SMTP"}
    ]

    for q in questions:
        print("\n" + q["question"])
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")
        
        answer_index = input("🔹 Wybierz odpowiedź (1-4): ").strip()
        
        if answer_index.isdigit():
            answer_index = int(answer_index) - 1  # Zamiana na indeks listy
            if 0 <= answer_index < len(q["options"]) and q["options"][answer_index] == q["correct"]:
                print("✅ Poprawna odpowiedź!")
            else:
                print(f"❌ Niepoprawna. Prawidłowa odpowiedź: {q['correct']}")
        
        print("\n" + "-" * 50)

if __name__ == "__main__":
    quiz()
