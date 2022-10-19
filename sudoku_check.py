#Vyřešení a kontrola správnosti všech sudoku ve složce sudokus.

from importlib.resources import path
import os
import time
from solver_functions import *

zav = []   #výsledky závislé kontroly
nez = []   #výsledky nezávislé kontroly

t0 = time.perf_counter()

path = os.path.dirname(os.path.realpath(__file__))

for sudoku in os.listdir(f'{path}\sudokus'):
    vysledek = vyres_sudoku(f'{path}\sudokus\{sudoku}', False)
    reseni = sudoku[:-4] + '_s.txt'
    try:   #provede závislou kontrolu, pokud existuje vzorové řešení
        zav.append(zkontroluj_sudoku(vysledek,f'{path}\solutions\{reseni}'))
    except FileNotFoundError:
        pass
    nez.append(zkontroluj_sudoku_nezavisle(vysledek))
    print(sudoku)

t1 = time.perf_counter()

for i in zav:
    chyby = 0
    if not i:
        chyby += 1
if chyby > 0:
    print('Závislá kontrola všech souborů: CHYBA')
else:
    print('Závislá kontrola všech souborů: V POŘÁDKU')
  
for i in nez:
    chyby = 0
    if not i:
        chyby += 1
if chyby > 0:
    print('Nezávislá kontrola všech souborů: CHYBA')
else:
    print('Nezávislá kontrola všech souborů: V POŘÁDKU')
    
print('Potřebný čas:', t1-t0 ,'s')