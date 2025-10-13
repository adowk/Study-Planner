# functions.py

Dette er fila der all logikken er. `main.py` bare viser menyen og snakker med brukeren, men arbeidet skjer her i `functions.py`.  
Det er tre parallelle lister til å lagre info om emner, og en stor liste med seks små lister inni til å lagre studieplanen (ett for hvert semester).

- `emnekoder` → alle emnekodene (f.eks. “DAT100”)  
- `semester_type` → Høst eller Vår for hvert emne (samme rekkefølge som emnekoder)  
- `studiepoeng` → antall studiepoeng (samme indeks som emnekodene)  
- `studieplan` → 6 semester (liste inni liste). Hver indre liste = emner i det semesteret.
