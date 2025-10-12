emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

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
            return    for s in studieplan:
        if kode in s:
            print(f"Emnet {kode} er allerede i studieplanen.")
            return
