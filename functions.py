emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

# TODO
# Skriv ut studieplan funksjon
# Sjekk for gyldighet
# Lagre dataen i en fil
# Les fra fil
# Rens fil


def lag_nytt_emne(kode, sem_type, sp):
    if kode in emnekoder:
        print(f"Emnet {kode} finnes allerede.")
        return
    emnekoder.append(kode)
    semester_type.append(sem_type)
    studiepoeng.append(sp)


def legg_til_i_studieplan(kode, semester):
    if kode not in emnekoder:
        print("Emnet finnes ikke.")
        return
    indeks = emnekoder.index(kode)
    semtype = semester_type[indeks]
    sp = studiepoeng[indeks]

    host_sem = [1, 3, 5]
    var_sem = [2, 4, 6]

    for s in studieplan:
        if kode in s:
            print(f"Emnet {kode} er allerede i studieplanen.")
            return
        for s in studieplan:
        if semtype == "Høst" and semester not in host_sem:
            print(f"{kode} er et høstemne og kan ikke legges til i semester {semester}.")
            return
        if semtype == "Vår" and semester not in var_sem:
            print(f"{kode} er et våremne og kan ikke legges til i semester {semester}.")
            return
        total_sp = sum(studiepoeng[emnekoder.index(k)] for k in studieplan[semester-1])
        if total_sp + sp > 30:
            print(f"Ikke plass i semester {semester}.")
            return
        studieplan[semester-1].append(kode)
        print(f"{kode} ble lagt til i semester {semester}.")


    def skriv_ut_studieplan:
    
