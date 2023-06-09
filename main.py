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

def print_sudoku():
    return 0

def insert_number(column:int, row:int, value:int):
    if column > 9 or column < 1 or row > 9 or row < 1:
        raise ValueError("Valore non valido")
    if sudoku_matrix[row-1][column-1] != 0:
        raise ValueError("Valore già inserito")
    sudoku_matrix[row-1][column-1] = value
    print_sudoku()

def get_suggestion():
    return 0

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
                    column = int(input("Inserisci la colonna: "))
                    row = int(input("Inserisci la riga: "))
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
            print("Valore non valido")
            print("Riprova \n")
            continue