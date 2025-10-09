emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

def lag_emne():
    kode = input("Emnekode: ").upper()
    semester = input("Høst eller vår: ").capitalize()
    poeng = int(input("Studiepoeng: "))
    emnekoder.append(kode)
    semestere.append(semester)
    studiepoeng.append(poeng)

def skriv_ut_emner():
    if len(emnekoder) == 0:
        print("Ingen emner registrert ennå.")
    else:
        for i in range(len(emnekoder)):
            print(f"{i+1}. {emnekoder[i]} ({semestere[i]}) - {studiepoeng[i]} stp")

def legg_til_emne():
    skriv_ut_emner()
    e = int(input("Hvilket emne vil du legge til? ")) - 1
    s = int(input("I hvilket semester vil du legge det til (1-6)? ")) - 1
    if 0 <= e < len(emnekoder) and 0 <= s < len(studieplan):
        studieplan[s].append(emnekoder[e])
        print(f"{emnekoder[e]} lagt til i semester {s+1}")
    else:
        print("Ugyldig valg.")
