import functions as f


def main():
    while True:
            print("1. Lag emne")
            print("2. Legg til emne")
            print("3. Skriv ut emner")
            print("4. Avslutt")
            valg = input("Velg et alternativ: ")

            if valg == "1":
                f.lag_emne()
            elif valg == "2":
                f.legg_til_emne()
            elif valg == "3":
                f.skriv_ut_emner()
            elif valg == "4":
                break

main()