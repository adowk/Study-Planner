from functions import lag_nytt_emne, legg_til_i_studieplan, skriv_ut_studieplan, sjekk_gyldighet, lagring_fil, rens_fil
import os

def clear():
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")
                
                
def main():
    while True:
        clear()
        print("\n=== STUDIEPLAN-MENY ===")
        print("1. Legg til nytt emne")
        print("2. Legg til emne i studieplan")
        print("3. Skriv ut studieplan")
        print("4. Sjekk om studieplanen er gyldig")
        print("5. Lagre til fil")
        print("6. Les til fil")
        print("7. Rens (tøm) alle filer")
        print("8. Avslutt")

        valg = input("Velg et alternativ (1–7): ")

        if valg == "1":
            kode = input("Skriv emnekode: ").upper()
            sem_type = input("Skriv semester (Vår/Høst): ").capitalize()
            sp = int(input("Antall studiepoeng: "))
            lag_nytt_emne(kode, sem_type, sp)

        elif valg == "2":
            kode = input("Skriv emnekode: ").upper()
            semester = int(input("Hvilket semester (1–6): "))
            legg_til_i_studieplan(kode, semester)

        elif valg == "3":
            skriv_ut_studieplan()
            input("\nTrykk Enter for å gå tilbake til menyen...")
            

        elif valg == "4":
            sjekk_gyldighet()
            input("\nTrykk Enter for å gå tilbake til menyen...")

        elif valg == "5":
            lagring_fil()
            print("Data lagret til fil.")
            input("\nTrykk Enter for å gå tilbake til menyen...")

        elif valg == "6":
            les_fil()
            skriv_ut_studieplan()
            input("\nTrykk Enter for å gå tilbake til menyen...")

               
            
        elif valg == "7":
            bekreft = input("Er du sikker på at du vil tømme alle filer? (ja/nei): ").lower()
            if bekreft == "ja":
                rens_fil()
                print("Alle filer er tømt.")
                input("\nTrykk Enter for å gå tilbake til menyen...")
            else:
                print("Avbrutt.")

        elif valg == "8":
            print("Avslutter programmet...")
            break

        else:
            print("Ugyldig valg – prøv igjen.")
            input("\nTrykk Enter for å gå tilbake til menyen...")

if __name__ == "__main__":
    main()
