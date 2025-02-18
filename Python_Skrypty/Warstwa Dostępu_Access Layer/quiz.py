import time
import sys

# Funkcja do szybkiego wypisywania tekstu
def fast_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 1. Animacja rozgłaszania ramki (Broadcast)
def animate_broadcast():
    fast_print("📡 [Switch] Otrzymano ramkę! Sprawdzanie tabeli MAC...", 0.05)
    fast_print("🔎 Adres docelowy MAC: FF:FF:FF:FF:FF:FF (Broadcast)")
    fast_print("📡 Wysyłanie do wszystkich portów oprócz wejściowego...")
    fast_print("✅ Ramka rozgłoszona!")

# 2. Nauka MAC (MAC learning)
def animate_mac_learning():
    fast_print("🧐 [Switch] Analiza przychodzącej ramki...")
    fast_print("🔍 Źródłowy MAC: 00:1A:2B:3C:4D:5E na porcie 1")
    fast_print("📋 Aktualizacja tabeli MAC...")
    fast_print("📊 Nowa tabela MAC:\n| Port | MAC Address       |\n|------|-------------------|\n| 1    | 00:1A:2B:3C:4D:5E |")

# 3. Forwarding ramki na odpowiedni port
def animate_switch_forwarding():
    fast_print("📡 Sprawdzanie tabeli MAC...")
    fast_print("✅ MAC 3C:97:0E:67:89:AB znajduje się na porcie 3!")
    fast_print("🚀 Przekierowanie ramki na port 3!")

# 4. Nieznany adres MAC - Flooding
def animate_unknown_mac():
    fast_print("❓ Adres MAC nieznany w tabeli MAC.")
    fast_print("📡 Rozgłaszanie ramki do wszystkich portów (Flooding)!")
    fast_print("✅ Wysłano do wszystkich aktywnych portów.")

# 5. Animacja enkapsulacji
def animate_encapsulation():
    fast_print("📦 Tworzenie ramki Ethernet...")
    headers = [
        "🔢 Dane: HTTP Request",
        "🔢 Nagłówek TCP: SRC 56789 | DST 443",
        "🌐 Nagłówek IP: SRC 192.168.1.10 | DST 10.0.0.5",
        "🔗 Nagłówek Ethernet: SRC 00:1A:2B:3C:4D:5E | DST 3C:97:0E:67:89:AB",
        "🔑 Dodawanie FCS (Frame Check Sequence)"
    ]
    for h in headers:
        fast_print(h, 0.05)
    fast_print("🚀 Ramka gotowa do wysłania!")

# 6. Host odrzuca niepasującą ramkę unicast
def animate_unicast_reject():
    fast_print("📥 Host odbiera ramkę...")
    fast_print("❌ MAC docelowy niezgodny! Ramka odrzucona.")

# 7. Weryfikacja błędów (FCS)
def animate_fcs_check():
    fast_print("📡 Analiza ramki pod kątem błędów...")
    fast_print("✅ Suma kontrolna FCS poprawna. Transmisja OK!")

# 8. Forwarding przy pełnej tabeli MAC
def animate_full_mac_forwarding():
    fast_print("📊 Tabela MAC kompletna. Adres docelowy znany.")
    fast_print("🚀 Przekazanie ramki do odpowiedniego portu.")

# 9. Switch dynamicznie aktualizuje tabelę MAC
def animate_mac_update():
    fast_print("📡 Switch otrzymuje nową ramkę...")
    fast_print("📋 Aktualizacja tabeli MAC...")
    fast_print("✅ Nowy adres zapisany!")

# 10. Ramka Unicast trafia do właściwego odbiorcy
def animate_unicast_forwarding():
    fast_print("📥 Ramka unicast odebrana.")
    fast_print("✅ MAC docelowy zgodny! Dostarczenie poprawne.")

# 11. Switch odbiera i przetwarza wiele ramek jednocześnie
def animate_parallel_processing():
    fast_print("⚡ Switch przetwarza wiele ramek równocześnie...")
    fast_print("✅ Wszystkie pakiety przesłane poprawnie!")

# Quiz
def quiz():
    questions = [
        ("🔎 Co zrobi przełącznik, gdy nie zna docelowego adresu MAC?",
         ["A: Wykona ARP request.",
          "B: Rozgłosi ramkę do wszystkich portów.",
          "C: Powiadomi hosta o błędzie.",
          "D: Wyśle ramkę do konkretnego portu."],
         "B", animate_unknown_mac),
        
        ("⚡ Które urządzenie przekazuje dane na podstawie tabeli MAC?",
         ["A: Hub", "B: Router", "C: Switch", "D: Modem"],
         "C", animate_mac_learning),
        
        ("📋 Jakie informacje zapisuje switch w tabeli MAC?",
         ["A: Adres IP docelowy.", "B: Adres MAC źródłowy.", "C: Adres IP źródłowy.", "D: Adres MAC docelowy."],
         "B", animate_mac_update),
        
        ("🛡️ Co robi pole FCS?",
         ["A: Pozyskuje adres MAC.", "B: Sprawdza błędy transmisji.", "C: Oblicza CRC.", "D: Kontroluje dostęp."],
         "B", animate_fcs_check),
        
        ("🔀 Jak działa switch warstwy 2?",
         ["A: Przekazuje dane na podstawie adresu MAC.", "B: Duplikuje sygnał do każdego portu.", "C: Analizuje adresy IP.", "D: Zatrzymuje pakiety na warstwie 1."],
         "A", animate_switch_forwarding),
        
        ("📦 Co to jest enkapsulacja?",
         ["A: Dekodowanie.", "B: Dodawanie nagłówków.", "C: Fragmentacja.", "D: Routing."],
         "B", animate_encapsulation),
        
        ("🔍 Jakie pola zawiera ramka Ethernet 802.3? (Wybierz trzy)",
         ["A: Adres MAC źródłowy", "B: Adres IP źródłowy", "C: FCS", "D: Adres MAC docelowy"],
         ["A", "C", "D"], animate_encapsulation),
        
        ("📝 Co zrobi host, jeśli odbierze ramkę unicast z niepasującym MAC?",
         ["A: Odrzuci ramkę.", "B: Przekieruje ją dalej.", "C: Usunie nagłówek Ethernet.", "D: Wykona ARP request."],
         "A", animate_unicast_reject),
        
        ("📡 Jak switch podejmuje decyzje o przekazywaniu ramek?",
         ["A: Na podstawie MAC.", "B: Na podstawie IP.", "C: Odrzuca nieznane MAC.", "D: Przekazuje wszystkie pakiety unicast."],
         "A", animate_full_mac_forwarding),

        ("📶 Co robi switch, gdy ma pełną tabelę MAC?",
         ["A: Odrzuca nowe adresy.", "B: Nadal przetwarza pakiety.", "C: Wysyła ARP request.", "D: Restartuje się."],
         "B", animate_full_mac_forwarding),

        ("⚡ Jak switch przetwarza wiele ramek jednocześnie?",
         ["A: Przetwarza je szeregowo.", "B: Używa buforowania.", "C: Blokuje nowe ramki.", "D: Odrzuca nadmiar ramek."],
         "B", animate_parallel_processing)
    ]
    
    for question, options, correct_answer, animation in questions:
        print("\n" + question)
        for option in options:
            print(option)
        
        answer = input("🔹 Wybierz odpowiedź: ").strip().upper()
        if answer == correct_answer or (isinstance(correct_answer, list) and sorted(answer) == sorted(correct_answer)):
            print("✅ Poprawna odpowiedź!")
        else:
            print(f"❌ Niepoprawna. Prawidłowa odpowiedź: {correct_answer}")
        
        animation()
        print("\n" + "-" * 50)

# Uruchomienie quizu
if __name__ == "__main__":
    quiz()
