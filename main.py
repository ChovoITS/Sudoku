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
    print("\n")
    for x in range(9):
        for y in range(9):
            print(sudoku_matrix[x][y], end=" ")
        print()
    print("\n")

def insert_number():
    return 0

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
            insert_number()
        case 3:
            get_suggestion()
        case 4:
            break
        case _:
            print("Valore non valido")
            print("Riprova \n")
            continue