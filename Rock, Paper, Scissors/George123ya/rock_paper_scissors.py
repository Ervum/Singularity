from time import sleep
import random

def error():
    print("Entrada inválida, volvamos a intentarlo!\n")
    pass

def decidir(j):
    print("Tú:     ", jugadas[j-1].capitalize())
    draw = jwins = cjwins = False
    cj = random.randint(1,3)
    print("Máquina:", jugadas[cj-1].capitalize())
    jugada = [j, cj]
    i_win = [[1, 3], [2, 1], [3, 2]]
    ia_wins = [[3, 1], [1, 2], [2, 3]]

    if jugada[0] == jugada[1]:
        draw = True
    elif jugada in i_win:
        jwins = True
    elif jugada in ia_wins:
        cjwins = True

    if draw:
        print("EMPATE\n")
    elif jwins:
        print("GANASTE :D.", jugadas[jugada[0]-1].capitalize() ,"le gana a", jugadas[jugada[1]-1] + ".\n")
    elif cjwins:
        print("PERDISTE :(.", jugadas[jugada[1]-1].capitalize() ,"le gana a", jugadas[jugada[0]-1] + ".\n")

jugadas = ["piedra", "papel", "tijeras"]

# for a in range(5):
while True:
    f = input("Vamos a jugar Piedra (1) Papel (2) o Tijera (3)! (ENTER para jugar / Q para salir)")
    if f.lower() == "q":
        break

    print("Piedra (1)")
    sleep(0.5)
    print("Papel (2)")
    sleep(0.5)
    print("O Tijeras! (3)")

    j = input("\n")
    print("")

    if j.isdigit():
        if float(j) % 1 == 0 and int(j) in range(1,4):
            j = int(j)
            decidir(j)
        else:
            error()
    elif j.lower() == "q":
        break
    else:
        error()

print("\nGracias por jugar, nos vemos!")
sleep(3)
