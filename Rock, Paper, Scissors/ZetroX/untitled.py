from random import randint 

options = ["piedra", "papel", "tijeras"]

# Descomentar el 1r return para poder jugar contra la IA
def resetGame():
    #return ( randint(0,2), int(input("Escoge un número de las opciones propuestas: \n0. Piedra\n1. Papel\n2. Tijeras" )))
    return ( randint(0,2), randint(0,2) )

for i in range(0, 10):
    players = resetGame() 

    diffOptions = abs( players[0] - players[1] )
    winner = "opponent"

    if players[0] % 2 == 0 and players[1] % 2 == 0:
        winner = "opponent" if players.index(min(players)) == 0 else "you"
    else :
        winner = "opponent" if players.index(max(players)) == 0 else "you"

    if diffOptions == 1:
        print(f"The winner is: {winner}")
    elif diffOptions == 0:
        print("Tie")
    else:
        print(f"The winner is: {winner}")

    print(f"Opponent: {options[players[0]]} || You: {options[players[1]]}\n" )
