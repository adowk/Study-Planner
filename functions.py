emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

def lag_emne():
  k = input("Emnekode: ").upper()
  s = input("Høst eller vår: ").capitalize()
  p = int(input("Studiepoeng: "))

  emnekoder.append(kode)
  semestere.append(semester)
  studiepoeng.append(poeng)
