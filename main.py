from functions import lag_emne, legg_til_emne, skriv_ut_emner, studieplan

while True:
    print("\n1. Registrer nytt emne")
    print("2. Vis emner")
    print("3. Legg til emne i studieplan")
    print("4. Vis studieplan")
    print("5. Avslutt")

    valg = input("Velg handling: ")

    if valg == "1":
        lag_emne()
    elif valg == "2":
        skriv_ut_emner()
    elif valg == "3":
        legg_til_emne()
    elif valg == "4":
        for i, semester in enumerate(studieplan, start=1):
            print(f"Semester {i}: {semester}")
    elif valg == "5":
        break
    else:
        print("Ugyldig valg.")
