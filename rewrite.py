from importlib.resources import path
import os

path = os.path.dirname(os.path.realpath(__file__))


#přepis zadání do vhodnějšího tvaru
for file in os.listdir(f'{path}\original_sudokus'):
    with open(f'{path}\original_sudokus\{file}', "r") as original_sudoku:   #načte soubor ze složky original_sudokus
        data = original_sudoku.read(170)   #načte zadání sudoku bez posledních 2 prázdných řádků
        data = data.replace('\n', '')
        data = list(data[::2])
        with open(f'{path}\sudokus\{file}', "w") as sudoku:   #vytvoří nový soubor ve složce sudokus
            sudoku.write(" ".join(data[0:9]))
            for i in range(1, 9):
                x = "\n" + " ".join(data[(0+9*i):(9+9*i)])
                sudoku.write(x)


#přepis vzorových řešení do vhodnějšího tvaru
for file in os.listdir(f'{path}\original_solutions'):
    with open(f'{path}\original_solutions\{file}', "r") as original_solution:   #načte soubor ze složky original_solutions
        data_reseni = original_solution.read(313)   #načte soubor bez poseledních 3 řádků
        data_reseni = list(data_reseni.replace('\n', ''))
        data_reseni = [str(s) for s in data_reseni if s.isdigit()]
        s = []
        for i in range(9):
            s.append(data_reseni[12*i:12*i+9])
        data_reseni = s
        del s
        data_reseni = [item for sublist in data_reseni for item in sublist]
        with open(f'{path}\solutions\{file}', "w") as solution:   #vytvoří nový soubor ve složce solutions
            solution.write(" ".join(data_reseni[0:9]))
            for i in range(1, 9):
                x = "\n" + " ".join(data_reseni[(0+9*i):(9+9*i)])
                solution.write(x)