import os
import time
import sys

# Kode warna ANSI untuk Terminal (Hijau Neon & Reset)
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

def clear():
    # Membersihkan layar (Windows: cls, Mac/Linux: clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.05):
    # Efek mengetik huruf per huruf
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Desain Mata (Frame 1: Terbuka Penuh)
eye_open = f"""{GREEN}
       .01111111111110.
     .010000000000000010.
    0100000011111100000010
   010000001100001100000010
   010000001100001100000010
    0100000011111100000010
     '010000000000000010'
       '01111111111110'{RESET}"""

# Desain Mata (Frame 2: Setengah Tutup)
eye_half = f"""{GREEN}
       .00000000000000.
     .000000000000000000.
    0000000000000000000000
   000000000000000000000000
   000000000000000000000000
    0000000000000000000000
     '000000000000000000'
       '00000000000000'{RESET}"""

# Desain Mata (Frame 3: Tertutup/Berkedip)
eye_closed = f"""{GREEN}
       .----------------.
     .--------------------.
    ------------------------
    ------------------------
    ------------------------
    ------------------------
     '--------------------'
       '----------------'{RESET}"""

def run_animation():
    try:
        while True:
            # Tampilkan Mata Terbuka
            clear()
            print(f"{CYAN}👨‍💻 SYSTEM ACCESS: GRANTED 👨‍💻{RESET}\n")
            print(eye_open)
            print(f"\n{CYAN}   > SCANNING TARGET...{RESET}")
            time.sleep(1.5) # Tahan 1.5 detik

            # Proses Berkedip (Cepat)
            clear()
            print(f"{CYAN}👨‍💻 SYSTEM ACCESS: GRANTED 👨‍💻{RESET}\n")
            print(eye_half)
            time.sleep(0.15)

            clear()
            print(f"{CYAN}👨‍💻 SYSTEM ACCESS: GRANTED 👨‍💻{RESET}\n")
            print(eye_closed)
            time.sleep(0.15)

            clear()
            print(f"{CYAN}👨‍💻 SYSTEM ACCESS: GRANTED 👨‍💻{RESET}\n")
            print(eye_half)
            time.sleep(0.15)

    except KeyboardInterrupt:
        # Jika user menekan Ctrl+C, program berhenti dengan rapi
        clear()
        print(f"{GREEN}[+] Koneksi terputus. Keluar dari sistem...{RESET}")

if __name__ == "__main__":
    clear()
    typing_effect(f"{CYAN}Initializing Hacker Eye Protocol...{RESET}\n", speed=0.03)
    time.sleep(1)
    run_animation()
