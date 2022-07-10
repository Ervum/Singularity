# === Library Importing ===
import random as rand
import sys

# === Settings ===
InfiniteMode = True
Plays = [1, 2, 3] #1. Rock; 2. Paper; 3. Scissors.
Winner = ""


# === Naming ===
AIName = ["Ann-droid", "Roy-bot", "Ethan-droid", "Alexan-droid", "Megan-droid"]
PlayersName = str(input("   How'd you like to be called?: "))

AIWinningPhrase = [
    "'U suck at this ",
    "'u took the L ",
    "'hehe I won! ",
    "'I promise next year I won't misbehave. ",
    "'Santa Clous brought me coal. "
]

AIWinningWord = [
    ":c'",
    "lmao'",
    "lol'",
    "xD'",
    "ez"
]


# === Def. Functions ===
def PlayerWins():
    global Winner
    Winner = PlayersName

    print("\n " + Winner + " won!")
    str(input(" You said: "))

    return Winner

def AIWins():
    global Winner
    Winner = AIName[rand.randint(0, 4)] # Everytime the loop runs, you play with a differently-named AI.

    print("\n " + Winner + " won!")
    print(" It says: " + AIWinningPhrase[rand.randint(0, 4)] + AIWinningWord[rand.randint(0, 4)])

    return Winner

def ModeSelection():
    print("\n \n   Menu:")
    print("   1. Play \n   2. The best of \n   3. Tie-breaker \n   4. Infinite mode \n   5. Quit")

    Gamemode = str(input("\n \n   Please, select a Game Mode: "))
    Gamemode = int(Gamemode)

    if Gamemode == 1:
        print ("\n" * 20)

        Game()
    elif Gamemode == 2:
        Matches = str(input("\n \n   How many matches do you want to play?: "))
        Matches = int(Matches)

        print ("\n" * 20)

        for I in range(Matches):
            Game()
    elif Gamemode == 3:
        print ("\n" * 20)
        
        while Winner == "":
            Game()
    elif Gamemode == 4:
        print ("\n" * 20)

        while InfiniteMode == True:
            Game()
    elif Gamemode == 5:
        sys.exit()
    else:
        print("   ERROR: Invalid action! \n")

def Game():
    print("\n \n   Options:")
    print("   1. Rock \n   2. Paper \n   3. Scissors \n   4. Menu \n   5. Quit \n")

    PlayerMove = str(input(" What will you play?: "))
    PlayerMove = int(PlayerMove)

    if PlayerMove == 4:
        print ("\n" * 20)

        ModeSelection()
    elif PlayerMove == 5:
        sys.exit()
    
    AIMove = Plays[rand.randint(0, 2)]
    print(" It played '" + str(AIMove) + "'!")

    PlayerMove *= 5
    AIMove *= 5
    RoundPlays = PlayerMove + AIMove
    
    if PlayerMove == 5 or PlayerMove == 10 or PlayerMove == 15:
        if (RoundPlays / 5) % 2 == 0:
            if PlayerMove == 5:
                PlayerWins()
            elif PlayerMove == 15:
                AIWins()
            else:
                print("\n The match ends in a tie!")
        else:
            if PlayerMove > AIMove:
                PlayerWins()
            else:
                AIWins()
    else:
        print(" ERROR: Invalid action! \n")


# === Game ===
ModeSelection()
