import time

def radek(i, cislo, data, p):
    """
    Funkce zkontroluje, zda se cislo už nachází v i-tém řádku podle "data".
    Vrací True, pokud ano, jinak False.
    """
    pocitadlo = 0
    for j in range(9):
        if data[i][j] == cislo:
            pocitadlo += 1
    if pocitadlo > 1:
        return True
    else:
        return False

def sloupec(j, cislo, data, p):
    """
    funkce zkontroluje, zda se cislo už nachází v j-tém sloupci podle "data",
    vrací True, pokud ano, jinak False
    """
    pocitadlo = 0
    for i in range(9):
        if data[i][j] == cislo:
            pocitadlo += 1
    if pocitadlo > 1:
        return True
    else:
        return False

def ctverec(i, j, cislo, data, p):
    """
    funkce zkontroluje, zda se cislo na pozici (i,j) už nachází v příslušném čtverci podle "data",
    vrací True, pokud ano, jinak False
    """
    pocitadlo = 0
    for ii in range(i-i%3,i-i%3+3):
        for jj in range(j-j%3,j-j%3+3):
            if data[ii][jj] == cislo:
                pocitadlo += 1
    if pocitadlo > 1:
        return True
    else:
        return False



def vyres_sudoku(zadani, informace):
    '''
    Funkce načte zadaní "zadani" a vyřeší jej.
    Pokud je volba "informace" nastavená jako True, funkce vrací počet předvyplněných políček, řešení sudoku jako dvourozměrné pole a čas, který byl potřebný k doplnění chybějících políček.
    Pokud je volba "informace" nastavená jako False, funkce vrací pouze řešení sudoku jako dvourozměrné pole.
    '''
    with open(zadani,"r") as sudoku:
        data = sudoku.read()
        data = data.replace('\n', ' ')
        data = list(data[::2])
        data = [int(cislo) for cislo in data]
        
        obtiznost = 0   #spočte počet předvyplněných políček
        for i in data:
            if i != 0:
                obtiznost += 1
        
        vypln = []   #záznam o tom, která políčka jsou už předvyplněná
        for i in range(81):
            if data[i] != 0:
                vypln.append(True)
            else:
                vypln.append(False)
                
        data = [data[x:x+9] for x in range(0,81,9)]
        
    t0 = time.perf_counter()   #začátek měření času
    
    #doplnění chybějících čísel
    p = 0   #pozice v sudoku
    while p < 81:
        #print(f'pozice = {p}')
        #for i in range(9):
        #    print(data[i])
        if vypln[p] == True:
            p += 1
        else:
            while data[p//9][p%9] == 0 or (data[p//9][p%9] < 10 and (radek(p//9, data[p//9][p%9], data, p) or sloupec(p%9, data[p//9][p%9], data, p) or ctverec(p//9, p%9, data[p//9][p%9], data, p))):
                data[p//9][p%9] += 1
            if data[p//9][p%9] == 10:
                data[p//9][p%9] = 0
                p -= 1
                while vypln[p] == True:
                    p -= 1
                data[p//9][p%9] += 1
            else:
                p += 1
    t1 = time.perf_counter()   #konec měření času
    
    if informace:
        return(data, f'Čas potřebný k doplnění chybějících políček: {t1 - t0} s', f'Počet předvyplněných políček: {obtiznost}')
    else:
        return data



def zkontroluj_sudoku(vysledek, reseni):
    '''
    Funkce porovná výsledek získaný řešičem vyres_sudoku a porovná jej se vzorovým řešením.
    Funkce vrací True, pokud se výsledek a vzorové řešení shodují, v opačném případě vrací False.
    '''
    with open(reseni) as sudoku:
        data_reseni = sudoku.read()
        data_reseni = data_reseni.replace('\n', ' ')
        data_reseni = list(data_reseni[::2])
        data_reseni = [int(cislo) for cislo in data_reseni]
        data_reseni = [data_reseni[x:x+9] for x in range(0,81,9)]
    chyby = 0
    for i in range(9):
        for j in range(9):
            if data_reseni[i][j] != vysledek[i][j]:
                chyby += 1
    if chyby > 0:        
        return False
    else:
        return True



def kontrola_radku(reseni):
    '''
    Funkce zkontroluje, zda se v každém řádku nachází každé číslo právě jednou.
    Vrací True, pokud ano, jinak False.
    '''
    chyby = 0
    for radek in reseni:
        cislo = 1
        Radek = sorted(radek)
        for i in Radek:
            if i != cislo:
                chyby += 1
            cislo += 1
    if chyby > 0:
        return False 
    else:
        return True        
    
def kontrola_sloupcu(reseni):
    '''
    Funkce zkontroluje, zda se v každém sloupci nachází každé číslo právě jednou.
    Vrací True, pokud ano, jinak False.
    '''
    chyby = 0
    reseni = list(map(list,zip(*reseni)))   #transponuje pole reseni, zbytek funkce je stejný jako kontrola_radku
    for radek in reseni:
        cislo = 1
        Radek = sorted(radek)
        for i in Radek:
            if i != cislo:
                chyby += 1
            cislo += 1
    if chyby > 0:
        return False 
    else:
        return True  

def kontrola_ctvercu(reseni):
    '''
    Funkce zkontroluje, zda se v každém čtverci nachází každé číslo právě jednou.
    Vrací True, pokud ano, jinak False.
    '''
    chyby = 0
    for i in range(3):   #prochází jednotlivé čtverce
        for j in range(3):
            ctverec = []
            for ii in range(3):   #zapíše prvky daného čtverce do seznamu ctverce
                for jj in range(3):
                    ctverec.append(reseni[3*i+ii][3*j+jj])
            cislo = 1
            Ctverec = sorted(ctverec)
            for k in Ctverec:
                if k != cislo:
                    chyby += 1
                cislo += 1
    if chyby > 0:
        return False 
    else:
        return True    

def zkontroluj_sudoku_nezavisle(vysledek):
    '''
    Funkce vyhodnotí, zda se ve vyřešeném sudoku nachází v každém řádku, sloupci a čtverci každé z čísel 1–9 právě jednou.
    Vrací True, pokud ano, jinak False.
    '''
    if kontrola_radku(vysledek) and kontrola_sloupcu(vysledek) and kontrola_ctvercu(vysledek):
        return True
    else:
        return False