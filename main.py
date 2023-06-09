from colorama import Fore, Style

sudoku_matrix = [[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]]

solution_matrix = [[5,3,4,6,7,8,9,1,2],
                    [6,7,2,1,9,5,3,4,8],
                    [1,9,8,3,4,2,5,6,7],
                    [8,5,8,7,6,1,4,2,3],
                    [4,2,6,8,5,3,7,9,1],
                    [7,1,3,9,2,4,8,5,6],
                    [9,6,1,5,3,7,2,8,4],
                    [2,8,7,4,1,9,6,3,5],
                    [2,4,5,2,8,6,1,7,9]]

def print_sudoku():
    print("\n")
    for x in range(9):
        for y in range(9):
            if sudoku_matrix[x][y] != 0:
                print(Fore.GREEN + str(sudoku_matrix[x][y]),end=" ")
                print(Style.RESET_ALL,end="")
            else:
                print(sudoku_matrix[x][y], end=" ")
            if y == 2 or y == 5:
                print("|", end=" ")
        print()
        if x == 2 or x == 5:
            print("---------------------",end="\n")
    print("\n")

def insert_number(column:int, row:int, value:int):
    if column > 9 or column < 1 or row > 9 or row < 1:
        raise ValueError("Valore non valido")
    if sudoku_matrix[row-1][column-1] != 0:
        raise ValueError("Valore già inserito")
    if solution_matrix[row-1][column-1] != value:
        print(Fore.RED + "Il valore inserito non corretto, Riprova")
        print(Style.RESET_ALL, end="")
        print(print_sudoku(row-1, column-1, True))
    else:
        sudoku_matrix[row-1][column-1] = value
        print_sudoku(row-1, column-1)

def get_suggestion():

    row = int(input("Il numero che vorresti conoscere in che riga si trova? "))
    column = int(input("Il numero che vorresti conoscere in che colonna si trova? "))
    if(sudoku_matrix[row-1][column-1] != 0):
        print(Fore.RED + 'Il numero richiesto è già pieno')
        print(Style.RESET_ALL, end="")
    else:
        print(f'Nella casella {row, column} il numero da mettere è {solution_matrix[row-1][column-1]}')

while True:
    try:
        answer = int(input("Menu \n \n1. Visualizza il sudoku \n2. Inserisci un numero \n3. Chiedi un suggerimento \n4. Exit \n"))
    except ValueError:
        raise ValueError("Valore non numerico")
    match answer:
        case 1:
            print_sudoku()
        case 2:
            while True:
                try:
                    row = int(input("Inserisci la riga: "))
                    column = int(input("Inserisci la colonna: "))
                    value = int(input("Inserisci il valore: "))
                except ValueError:
                    raise ValueError("Valore non numerico")
                if column > 9 or column < 1 or row > 9 or row < 1:
                    print(Fore.RED + "Valore delle colonne o delle righe non valido")
                    print(Style.RESET_ALL)
                elif sudoku_matrix[row-1][column-1] != 0:
                    print(Fore.RED + "Valore già inserito")
                    print(Style.RESET_ALL)
                else:
                    break
            insert_number(column, row, value)
        case 3:
            get_suggestion()
        case 4:
            break
        case _:
            print(Fore.RED + "Valore non valido")
            print(Style.RESET_ALL, end="")
            print("Riprova \n")
            continue