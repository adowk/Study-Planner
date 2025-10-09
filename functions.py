
emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

def lag_emne():
  print(emnekoder, semestere, studiepoeng, studieplan)

  kode = input("Emnekode: ").upper()
  semester = input("Høst eller vår: ").capitalize()
  poeng = int(input("Studiepoeng: "))
  emnekoder.append(kode)
  semestere.append(semester)
  studiepoeng.append(poeng)

  def skriv_ut_emner():
    print(emnekoder, semestere, studiepoeng, studieplan)
    if len(emnekoder) == 0:
        print("Ingen emner registrert ennå.")
    else:
        for i in range(len(emnekoder)):
            print(f"{i+1}. {emnekoder[i]} ({semestere[i]}) - {studiepoeng[i]} stp")

def legg_til_emne():
  print(emnekoder, semestere, studiepoeng, studieplan)
  skriv_ut_emner()
  e = int(input("Hvilket emne vil du legge til? "))
  s = int(input("I hvilket semester vil du legge det til (1-6)? "))
  emnekoder.append(e)
  semestere.append(s)
 
