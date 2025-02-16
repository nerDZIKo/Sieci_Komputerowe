import time
import sys

def animate_frame_transfer():
    frames = [
        "[  ]",  # Pusta ramka
        "[D ]",  # Dodanie adresu docelowego
        "[DS]",  # Dodanie adresu źródłowego
        "[DST]",  # Dodanie typu i długości
        "[DSTP]",  # Dodanie danych
        "[DSTPF]",  # Dodanie sumy kontrolnej
    ]
    
    print("Tworzenie ramki Ethernet:")
    for frame in frames:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\nRamka została wysłana!\n")
    
    print("Dekapsulacja na odbiorniku:")
    for frame in reversed(frames):
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\nDane odebrane i przetworzone!")

if __name__ == "__main__":
    animate_frame_transfer()
