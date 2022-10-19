from solver_functions import *   #importuje funkce pro řešení sudoku a kontroly správnosti sudoku
from tkinter import Tk, Entry, Button, Label

root = Tk()
root.geometry("500x100+200+200")

my_text = Label(root, text='Zadejte ze složky "sudoku" název souboru, který chcete vyřešit.')
my_text.pack()

entry = Entry(root)
entry.pack()

import os
path = os.path.dirname(os.path.realpath(__file__))

def function():
    try:
        data = vyres_sudoku(f'{path}\sudokus\{entry.get()}', True)
        root_data = Tk()
        root_data.geometry("500x400+800+200")
        
        nazev = Label(root_data, text=f'{entry.get()}\n')   #název souboru
        nazev.pack()

        vysledek = ''
        for i in range(9):
            x = [str(j) for j in data[0][i]]
            x = '   '.join(x)
            vysledek = vysledek + f'{x}\n'
        
        text = Label(root_data, text=f'{vysledek}')   #vyplněné sudoku
        text.config(font=('times', 18, 'bold'))
        text.pack()
        
        #kontroly
        reseni = f'{path}\solutions\{entry.get()}'[:-4] + '_s.txt'
        try:   #provede závislou kontrolu, pokud existuje vzorové řešení
            zav = zkontroluj_sudoku(data[0], reseni)
        except FileNotFoundError:
            zav = 'Vzorové řešení neexistuje.'
        
        nez = zkontroluj_sudoku_nezavisle(data[0])
        
        if zav == True:
            zav = "V POŘÁDKU"
        elif zav == False:
            zav = "CHYBA"
        if nez:
            nez = "V POŘÁDKU"
        else:
            nez = "CHYBA"
        
        text2 = Label(root_data, text=f'Porovní se vzorovým řešením: {zav}\nNezávislá kontrola: {nez}')   #výsledky kontrol
        text2.pack()
        
        text3 = Label(root_data, text=f'{data[1]}\n{data[2]}' )  #doba trvaní řešení, počet předvyplněných políček
        text3.pack()
        
        root_data.mainloop()
    except FileNotFoundError:
        root_chyba =Tk()
        root_chyba.geometry("250x50+325+200")
        text_chyba = Label(root_chyba, text='Soubor neexistuje.')
        text_chyba.pack()
        root_chyba.mainloop()

button = Button(root, text='Vyřešit', command=function)
button.pack()

root.mainloop()