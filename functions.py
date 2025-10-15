import os
emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

# TODO
# Skriv ut studieplan funksjon | DONE
# Sjekk for gyldighet | DONE
# Lagre dataen i en fil | DONE
# Les fra fil | DONE
# Rens fil | DONE


def lag_nytt_emne(kode, sem_type, sp):
    if kode in emnekoder:
        print(f"Emnet {kode} finnes allerede.")
        return
    emnekoder.append(kode)
    semestere.append(sem_type)
    studiepoeng.append(sp)


def legg_til_i_studieplan(kode, semester):
    if kode not in emnekoder:
        print("Emnet finnes ikke.")
        return
    indeks = emnekoder.index(kode)
    semtype = semestere[indeks]
    sp = studiepoeng[indeks]

    host_sem = [1, 3, 5]
    var_sem = [2, 4, 6]

    for s in studieplan:
        if kode in s:
            print(f"Emnet {kode} er allerede i studieplanen.")
            return
    if semtype == "Høst" and semester not in host_sem:
        print(f"{kode} er et høstemne og kan ikke legges til i semester {semester}.")
        return
    if semtype == "Vår" and semester not in var_sem:
        print(f"{kode} er et våremne og kan ikke legges til i semester {semester}.")
        return

    total_sp = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[semester - 1])
    if total_sp + sp > 30:
        print(f"Ikke plass i semester {semester}.")
        return

    studieplan[semester - 1].append(kode)
    print(f"{kode} ble lagt til i semester {semester}.")


def skriv_ut_studieplan():
    for i, sem in enumerate(studieplan, start=1):
        print(f"Semester {i}:")
        if not sem:
            print("  Ingen emner")
        else:
            for kode in sem:
                idx = emnekoder.index(kode)
                print(f"  {kode} ({studiepoeng[idx]} sp)")


def sjekk_gyldighet():
    gyldig = True
    for i, sem in enumerate(studieplan, start=1):
        total_sp = sum(studiepoeng[emnekoder.index(k)] for k in sem)
        if total_sp != 30:
            gyldig = False
            print(f"Semester {i} er ikke gyldig ({total_sp} / 30 sp)")
    if gyldig:
        print("Studieplanen er gyldig!")

BASE_PATH = r"C:\Users\adamo\Documents\Prog\Oving 6"
def lagring_fil():
    """
    print("Lagrer til fil ...")
    print("Emnekoder:", emnekoder)
    print("Semestere:", semestere)
    print("Studiepoeng:", studiepoeng)
    print("Studieplan:", studieplan)
    """
    with open(os.path.join(BASE_PATH, "emner.txt"), "w", encoding="UTF-8") as f:
            for e in emnekoder:
                f.write(f"{e}\n")

    with open(os.path.join(BASE_PATH, "semestere.txt"), "w", encoding="UTF-8") as f:
        for s in semestere:
            f.write(f"{s}\n")

    with open(os.path.join(BASE_PATH, "studiepoeng.txt"), "w", encoding="UTF-8") as f:
        for sp in studiepoeng:
            f.write(f"{sp}\n")

    with open(os.path.join(BASE_PATH, "studieplan.txt"), "w", encoding="UTF-8") as f:
        for sem in studieplan:
            f.write(",".join(sem) + "\n")


def les_fil():
    with open ("emner.txt", "r", encoding="UTF-8") as fil:
        for line in fil:
            emnekoder.append(line.strip())
    with open ("semestere.txt", "r", encoding="UTF-8") as fil:
        for line in fil:
            semestere.append(line.strip())
    with open ("studieplan.txt", "r", encoding="UTF-8") as fil:
        for line in fil:
            studieplan.append(line.strip())
    with open ("studiepoeng.txt", "r", encoding="UTF-8") as fil:
        for line in fil:
            studiepoeng.append(line.strip())

def rens_fil():
    open("emner.txt", "w").close()
    open("semestere.txt", "w").close()
    open("studieplan.txt", "w").close()
    open("studiepoeng.txt", "w").close()
