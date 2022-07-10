# === Library Importing === #
import random as Rand 
import ctypes as Wind
import sys as SYS


# === Window === #
Wind.windll.kernel32.SetConsoleTitleW("[1A] - Testing Game")


# === Def. Functions === #
def WipeScreen(WipeAmount, Input):
    if Input != "":
        input("\n \n Press 'enter' to " + Input + "...")

    print("\n" * WipeAmount)

def Error(ErrorMSG, Type, Exit):
    if Type == "Err":
        print("\n \n ERROR: " + ErrorMSG + "!")

        SYS.exit()
    elif Type == "Warn":
        print("\n   WARNING: " + ErrorMSG + "!")
    elif Type == "Adv":
        print("\n ADVICE: " + ErrorMSG + "!")
    else:
        print("\n " + ErrorMSG)

        if Exit == True:
            SYS.exit()

def GuessNumber(Min, Max):
       WipeScreen(100, "play")

       Answer = Rand.randint(Min, Max)
       Input = int(input(" Guess a number between " + str(Min) + " and " + str(Max) + ": "))

       if Input == Answer:
           print("\n \n   ~ CONGRATULATIONS! ~ \n   You guessed the number!")

           input("\n Laugh at the AI: ")
           input("\n \n Press 'enter' to play again...")

           GamemodeSelection()
       else:
           print("\n \n   ~ SO BAD! ~ \n   The number was " + str(Answer) + "!")

           input("\n \n Press 'enter' to play again...")

           GamemodeSelection()

def GamemodeSelection():
    Gamemodes = (1, 2, 3, 4, 5)

    WipeScreen(100, "")
    print("   GAMEMODES: \n   1. Effortless \n   2. Easy \n   3. Hard \n   4. Insane \n   5. Custom")

    Input = int(input("\n \n What gamemode will you play on?: "))

    if not Input in Gamemodes:
        Error("Gamemode doesn't exist", "Err", False)
    else:
        Game(int(Input))

def Game(Gamemode):
    if Gamemode == 1:
        GuessNumber(1, 5)
    elif Gamemode == 2:
        GuessNumber(1, 10)
    elif Gamemode == 3:
        GuessNumber(1, 25)
    elif Gamemode == 4:
        GuessNumber(1, 50)
    elif Gamemode == 5:
        WipeScreen(100, "")

        MIN = int(input(" What should be the MIN. the AI should randomize to?: "))
        MAX = int(input(" What should be the MAX. the AI should randomize to?: "))

        GuessNumber(MIN, MAX)


# === Game === #
GamemodeSelection()
