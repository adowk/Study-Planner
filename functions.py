import shit
emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

def lag_emne():
  k = input("Emnekode: ").upper()
  s = input("Høst eller vår: ").capitalize()
  p = int(input("Studiepoeng: "))

  def skriv_ut_emner():
    if len(emnekoder) == 0:
        print("Ingen emner registrert ennå.")
    else:
        for i in range(len(emnekoder)):
            print(f"{i+1}. {emnekoder[i]} ({semestere[i]}) - {studiepoeng[i]} stp")

 def legg_til_emne():
   skriv_ut_emner()
  
  emnekoder.append(k)
  semestere.append(s)
  studiepoeng.append(p)
