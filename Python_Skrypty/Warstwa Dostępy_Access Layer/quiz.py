import time
import sys

# Funkcja do stopniowego wypisywania tekstu
def slow_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 1. Animacja rozgłaszania ramki (broadcast)
def animate_broadcast():
    slow_print("📡 [Switch] Otrzymano ramkę! Sprawdzanie tabeli MAC...", 0.07)
    time.sleep(1)
    slow_print("🔎 Adres docelowy MAC: FF:FF:FF:FF:FF:FF (Broadcast)")
    slow_print("📡 Wysyłanie do wszystkich portów oprócz wejściowego...")
    time.sleep(1)
    slow_print("✅ Ramka rozgłoszona!")

# 2. Nauka MAC (MAC learning)
def animate_mac_learning():
    slow_print("🧐 [Switch] Analiza przychodzącej ramki...")
    time.sleep(1)
    slow_print("🔍 Źródłowy MAC: 00:1A:2B:3C:4D:5E na porcie 1")
    slow_print("📋 Aktualizacja tabeli MAC...")
    time.sleep(2)
    slow_print("📊 Tabela MAC:\n+------+-------------------+\n| Port | MAC Address       |\n+------+-------------------+\n| 1    | 00:1A:2B:3C:4D:5E |\n+------+-------------------+")

# 3. Forwarding ramki na odpowiedni port
def animate_switch_forwarding():
    slow_print("📡 Przełącznik sprawdza tabelę MAC...")
    time.sleep(1)
    slow_print("✅ MAC 3C:97:0E:67:89:AB znajduje się w tabeli na porcie 3!")
    slow_print("🚀 Przekierowanie ramki na port 3!")

# 4. Nieznany adres MAC
def animate_unknown_mac():
    slow_print("❓ Adres MAC 3F:45:67:89:AB:CD nieznany w tabeli MAC.")
    time.sleep(1)
    slow_print("📡 Rozgłaszanie ramki do wszystkich portów (Flooding)!")
    slow_print("✅ Wysłano do wszystkich aktywnych portów.")

# 5. Animacja enkapsulacji
def animate_encapsulation():
    slow_print("📦 Przygotowanie ramki Ethernet...", 0.07)
    headers = [
        "🔢 Dane użytkownika: HTTP GET Request",
        "🔢 Nagłówek TCP: [SRC: 56789 | DST: 443] + Checksum",
        "🌐 Nagłówek IP: [SRC: 192.168.1.10 | DST: 10.0.0.5] + TTL + Checksum",
        "🔗 Nagłówek Ethernet: [SRC: 00:1A:2B:3C:4D:5E | DST: 3C:97:0E:67:89:AB]",
        "🔑 Dodawanie FCS (Frame Check Sequence)"
    ]
    for h in headers:
        slow_print(h, 0.1)
        time.sleep(1)
    slow_print("🚀 Ramka gotowa do wysłania!")

# 6. Quiz z animacjami i rozbudowanymi odpowiedziami
def quiz():
    questions = [
        ("🔎 Co zrobi przełącznik, gdy nie zna docelowego adresu MAC?",
         ["A: Wyrzuci ramkę, ponieważ nie wie, dokąd ją przesłać",
          "B: Wykona operację floodingu – wyśle ramkę do wszystkich portów oprócz wejściowego, aby znaleźć właściwego odbiorcę"],
         "B", animate_unknown_mac),
        
        ("⚡ Które urządzenie przekazuje dane na podstawie tabeli MAC?",
         ["A: Hub – urządzenie warstwy 1, które po prostu powiela sygnał",
          "B: Router – przekazuje dane w oparciu o adresy IP",
          "C: Przełącznik – wykorzystuje tabelę MAC do przesyłania ramek do odpowiednich portów"],
         "C", animate_mac_learning),
        
        ("📋 Jakie informacje są używane do budowy tabeli MAC?",
         ["A: Przełącznik uczy się na podstawie docelowych adresów MAC w odbieranych ramkach",
          "B: Przełącznik zapamiętuje źródłowe adresy MAC i kojarzy je z portem, na którym je odebrał"],
         "B", animate_mac_learning),
        
        ("🛡️ Jaki jest cel pola FCS?",
         ["A: Umożliwia przełącznikowi sprawdzenie integralności ramki, wykrywając ewentualne błędy transmisji",
          "B: Zawiera dodatkowe informacje o źródłowym adresie MAC"],
         "A", animate_encapsulation),
        
        ("🚨 Co robi host, gdy MAC nie pasuje?",
         ["A: Odrzuca ramkę, ponieważ nie jest jej adresatem",
          "B: Wysyła ramkę do następnego urządzenia w sieci"],
         "A", animate_broadcast),
        
        ("🔀 Jak działa przełącznik warstwy 2?",
         ["A: Analizuje pakiety na podstawie adresów IP i wykorzystuje tablicę routingu",
          "B: Analizuje ramki na podstawie adresów MAC i kieruje je do odpowiednich portów"],
         "B", animate_switch_forwarding),
        
        ("📦 Co to jest enkapsulacja?",
         ["A: Proces dodawania nagłówków i stopki do danych w kolejnych warstwach modelu OSI",
          "B: Proces dekodowania pakietów w celu ich przesłania"],
         "A", animate_encapsulation),
        
        ("🤷 Co robi switch, gdy nie zna docelowego MAC?",
         ["A: Kasuje ramkę, ponieważ nie ma odpowiedniego wpisu w tabeli MAC",
          "B: Wysyła do wszystkich portów oprócz wejściowego, aby znaleźć prawidłowego odbiorcę"],
         "B", animate_unknown_mac),
        
        ("🔍 Jakie pola ma ramka Ethernet?",
         ["A: Źródłowy adres MAC – identyfikujący nadawcę",
          "B: Pole FCS – służące do wykrywania błędów",
          "C: Docelowy adres MAC – wskazujący odbiorcę"],
         "ABC", animate_encapsulation),
        
        ("📝 Jak działa forwarding w switchu?",
         ["A: Przełączniki uczą się, analizując źródłowe adresy MAC przychodzących ramek i aktualizując tabelę MAC",
          "B: Ramki adresowane do nieznanych MAC są automatycznie usuwane"],
         "A", animate_switch_forwarding)
    ]
    
    for question, options, correct_answer, animation in questions:
        print("\n" + question)
        for option in options:
            print(option)
        
        answer = input("🔹 Wybierz odpowiedź: ").strip().upper()
        if answer == correct_answer:
            print("✅ Poprawna odpowiedź!")
        else:
            print(f"❌ Niepoprawna. Prawidłowa odpowiedź: {correct_answer}")
        
        animation()
        print("\n" + "-" * 50)

# Uruchomienie quizu
def main():
    quiz()
    
if __name__ == "__main__":
    main()
