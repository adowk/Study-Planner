emnekoder = []
semestere = []
studiepoeng = []
studieplan = [[], [], [], [], [], []]

def lag_emne():
  k = input("Emnekode: ").upper()
  s = input("Høst eller vår: ").capitalize()
  p = int(input("Studiepoeng: "))

  emnekoder.append(k)
  semestere.append(s)
  studiepoeng.append(p)
