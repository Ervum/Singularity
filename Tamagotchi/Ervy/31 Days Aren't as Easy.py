# === Library Importing === #
import random as Rand 
import ctypes as Wind
import sys as SYS


# === Window === #
Wind.windll.kernel32.SetConsoleTitleW("[31 Days Aren't as Easy] - Testing Game")


# === Settings === #
Money = 500
Day = 1

Action = None
Place = None

PetName = None
PetHunger = 0 # Min - 0; Max - 100 (dead).
PetEnergy = 100 # Min - 0 (dead); Max - 100.
PetFood = 1
PetBed = 0
Pet = 0

RentPaid = 0 # 0. Default (hasn't happened); 1. True.
TipsON = 0 # 0. Default (false); 1. True; 2. False.


# === Def. Functions === #
def WipeScreen(WipeAmount):
    print("\n" * WipeAmount)

def ERROR(ErrorMSG):
    WipeScreen(30)

    print(" ERROR: " + ErrorMSG + "\n")
    Home()

def ProceedBuying(MSG):
    WipeScreen(50)

    if MSG != "":
        print(MSG)
    else:
        pass

    input("\n \n Press 'enter' to go back home...")

    WipeScreen(30)
    Home()

def Work():
    global Money

    WipeScreen(30)
    print(" ~ WORK AS A MATHEMATICIAN! ~ ")

    Number = [Rand.randint(0, 100), Rand.randint(0, 100)]
    Symbols = ["+", "-"]
    Symbol = Symbols[Rand.randint(0, 1)]
    Result = None

    if str(Symbol) == "+":
        Result = Number[0] + Number[1]
    elif str(Symbol) == "-":
        Result = Number[0] - Number[1]

    Answer = int(input((" BOSS: What is '" + str(Number[0]) + " " + Symbol + " " + str(Number[1]) + "', employee?: ")))

    if Answer == Result:
        Payment = Rand.randint(5, 80)
        Money += Payment

        print("\n ~ CONGRATULATIONS! ~")
        print(" You received $" + str(Payment) + "! You store it on your bank (for a total of $" + str(Money) + ").")
        
        input("\n \n Press 'enter' to get to the next day...")

        WipeScreen(80)
        NextDay()
    else:
        print(" BOSS: GET OUT of here and DON'T COME BACK ever again!")

        input("\n Excuse yourself: ")

        WipeScreen(100)
        print("It didn't work;")

        if Pet == 0:
            if Day == 27:
                print("you were fired from your job and couldn't afford to pay the monthly rent. The landlord brought bandits to your home; they kicked you out and you died yourself out of hunger on the lively streets at night, February " + str(Day + Rand.randint(1, 3)) + ". \n")
            else:
                print("you were fired from your job and couldn't afford to pay the monthly rent. The landlord brought bandits to your home; they kicked you out and you died yourself out of hunger on the lively streets at night, January " + str(Day + Rand.randint(2, 5)) + ". \n")
        else:
            if Day == 26:
                print("you were fired from your job and couldn't afford to pay the monthly rent. The landlord brought bandits to your home; they kicked you out and you died yourself out of hunger on the lively streets at night, after eating your Pet, February " + str(Rand.randint(2, 4)) + ". \n")
            else:
                print("you were fired from your job and couldn't afford to pay the monthly rent. The landlord brought bandits to your home; they kicked you out and you died yourself out of hunger on the lively streets at night, after eating your Pet, January " + str(Day + Rand.randint(3, 6)) + ". \n")
        
    return Money
def ThirdSecretEnding():
        print("   The letter promised 'HoUse CO'd get you out off your house. Nevertheless, the Landlord'd rather pay bandits which, actually, were much cheaper. They kicked you out and you died out of hunger on the lively streets at night, January 31."); 

        input("\n \n Press 'enter' to continue reading...")

        WipeScreen(200)
        print("   ~ 3rd SECRET ENDING - CONGRATULATIONS! ~")

def Home():
    global PetEnergy
    global PetHunger

    global RentPaid

    global PetFood
    global PetName
    global PetBed

    global Money

    WipeScreen(30)
    print(" Your home, once again, has this scent which resembles the past, calm days.")

    if Day == 25 and RentPaid == 0:
        if Pet == 1:
            ThirdSecretEnding()   
            print("   You died on the verge of the end of the month, out of hunger, together with your Pet. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")

            SYS.exit()
        else:
            ThirdSecretEnding()   
            print("   You died on the verge of the end of the month, out of hunger, all alone. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")

            SYS.exit()

    if Pet == 1:
        if PetEnergy <= 0 or PetHunger >= 100:
            print(" Despite your Pet having died in misery on a corner of your room.")

            input("\n \n Press 'enter' to continue reading...")

            WipeScreen(200)
            print("   ~ 1st SECRET ENDING - CONGRATULATIONS! ~")
            print("   You got out alive and died several decades later, but not your Pet. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")
        
            SYS.exit()

        if PetEnergy > 100:
            PetEnergy = 100
        elif PetEnergy < 0:
            PetEnergy = 0

        PetEnergy -= Rand.randint(20, 40)

        if PetHunger < 0:
            PetHunger = 0
        elif PetHunger > 100:
            PetHunger = 100

        if PetName == None:
            print(" The only thing that makes you vigilant, is the egg hatching from several hours ago. In fact, a being it's already coming out of it...")

            PetName = str(input("\n \n How'd you like to name your Pet?: "))

            print(" That's a lovely name! I'm sure " + PetName + " liked it!")
            input("\n \n Press 'enter' to get to the next day...")

            WipeScreen(100)
            Home()
        else:
            print(" Your Pet gets you on the floor and starts kissing your face. You're happy at last.")
            print("\n You have " + str(PetFood) + "g of food.")
            print("\n \n   The STATE of your Pet is the following: \n   | Energy: " + str(PetEnergy) + "%;\n   | Hunger: " + str(PetHunger) + "%.")
    
    if Day == 21:
        print("\n \n There's a letter on the door. You know who it is from, and subsequently, as if accepting what's going to happen, open it; \n \n")

        print(" ~------------------------------------------------------------------------------------------~")
        print(" Esteemed: \n the rent ($350) must be paid within the next three (3) days; otherwise, the tenant will be evicted from the house and 'HoUse CO.' will keep the tenant's belongings until the completion of their duties. \n \n Yours Faithfully.")
        print(" ~------------------------------------------------------------------------------------------~")
    
    if Day == 22 or Day == 23 or Day == 24:
        if RentPaid == 0:
            print("\n \n The rent must be paid on the NEAR future.")

    if TipsON == 1:
        print("\n \n   ACTIONS: \n   1. Sleep (-> next day) \n   2. Work (-> next day, +money)")

        if Pet == 1:
            print("\n   PET ACTIONS: \n   3. Feed (+energy, -hunger) \n   4. Stroke (+energy)")
        
        if Day == 21 or Day == 22 or Day == 23 or Day == 24:
            if RentPaid == 0:
                print("\n   RENT ACTIONS: \n   5. Pay")
    else:
        print("\n \n   ACTIONS: \n   1. Sleep \n   2. Work")

        if Pet == 1:
            print("\n   PET ACTIONS: \n   3. Feed \n   4. Stroke")
        
        if Day == 21 or Day == 22 or Day == 23 or Day == 24:
            if RentPaid == 0:
                print("\n   RENT ACTIONS: \n   5. Pay")
                
    Action = int(input("\n What will you do?: "))

    if Action == 1:
        input("\n \n Press 'enter' to sleep...")

        WipeScreen(80)
        NextDay()
    elif Action == 2:
        Work()
    elif Action == 3:
        if Pet == 1:
            if PetHunger > 0:
                if PetFood > 0:
                    WipeScreen(50)
                    print(" You have " + str(PetFood) + "g of food.")
                    Feed = int(input("\n How many times do you want to feed " + PetName + "?: "))

                    if Feed > PetFood:
                        input("\n \n YOU: But I don't have that much food...")
                        input("\n \n Press 'enter' to go back home...")

                        WipeScreen(50)
                        Home()
                    else:
                        PetFood -= Feed 

                        PetEnergy += 10 * PetFood
                        PetHunger -= 5 * PetFood

                        input("\n \n The smile on your Pet's face makes your day much easier. What's that on it's tooth, though?")
                        input("\n \n Press 'enter' to go to the next day...")

                        WipeScreen(80)
                        NextDay()
                else:
                    input("\n \n YOU: But I don't have any food to give " + PetName + "...")

                    WipeScreen(80)
                    NextDay()
            else:
                input("\n \n YOU: I don't think it's hungry...")
                    
                WipeScreen(80)
                NextDay()
        else:
            ERROR("Invalid action (" + str(Action) + ")!")
    elif Action == 4:
        if Pet == 1:
            if PetBed == 1:
                PetEnergy += Rand.randint(35, 85)
                PetHunger += Rand.randint(5, 10)
            else:
                PetEnergy += Rand.randint(25, 70)
                PetHunger += Rand.randint(5, 10)
                
                WipeScreen(50)

                input(" Seeing " + PetName + " rubbing against your hand, as it's hair bristles with happiness it's refreshing for you.")
                input("\n \n Press 'enter' to go to the next day...")
                
                WipeScreen(80)
                NextDay()
        else:
            ERROR("Invalid action (" + str(Action) + ")!")
    elif Action == 5:
        if Day == 21 or Day == 22 or Day == 23 or Day == 24:
            if RentPaid == 0:
                if Money >= 350:
                    Money -= 350
                    RentPaid = 2

                    WipeScreen(50)
                    print(" You paid the rent!")

                    input("\n \n Press 'enter' to go to the next day...")
                        
                    WipeScreen(80)
                    NextDay()
                else:
                    ProceedBuying(" Insufficient funds!")
            else:
                ERROR("Invalid action (" + str(Action) + ")!")
        else:
            ERROR("Invalid action (" + str(Action) + ")!") 
    else:
        ERROR("Invalid action (" + str(Action) + ")!")

    return PetEnergy, PetHunger, RentPaid, PetFood, PetName, Money

def Shop():
    global PetFood
    global PetBed
    global Pet

    global Money

    WipeScreen(30)
    print(" You have $" + str(Money) + ".")
    print(" You see a showcase with a big variety of objects on it.")

    if TipsON == 1:
        print("\n \n   SHOWCASE: \n   1. An egg - $120 \n   2. A handful of pet food (gain energy) - $5 \n   3. A pet's immaculate bed (recovers energy faster) - $170")
    else:
        print("\n \n   SHOWCASE: \n   1. An egg - $120 \n   2. A handful of pet food - $5 \n   3. A pet's immaculate bed - $170")
    
    Item = int(input("\n What will you buy?: "))

    if Item == 1:
        if Money >= 120:
            if Pet == 1:
                WipeScreen(30)
                print(" YOU: It'd be cruel of me to get another pet which I cannot take responsibility of.")

                ProceedBuying("")
            else:
                Money -= 120
                Pet = 1

                ProceedBuying(" Sucessfully bought 'Pet Egg'!")
                print("\n \n How'd you like to name your Pet?: ")
        else:
            ProceedBuying(" You don't have enough money! Come back again later.")
            
    elif Item == 2:
        if Money >= 5:
            if PetFood < 10:
                Money -= 5
                PetFood += 1

                ProceedBuying(" Sucessfully bought 1g of 'Pet Food (for a total of " + str(PetFood) +"g)'!")
            else:
                WipeScreen(30)
                print(" YOU: But I already do have 10g of this; why'd I want more?.")

                ProceedBuying("")
        else:
            ProceedBuying(" You don't have enough money! Come back again later.")
    elif Item == 3:
        if Money >= 170:
            if Pet != 1:
                WipeScreen(30)
                print(" YOU: Why'd I buy this bed when I don't have any pets?")

                input("\n \n Press 'enter' to continue playing...")
        
                WipeScreen(30)
                Home()
            elif PetBed == 1:
                WipeScreen(30)
                print(" YOU: Why'd I buy this bed once again?")

                input("\n \n Press 'enter' to continue playing...")
        
                WipeScreen(30)
                Home()
            else:
                Money -= 170
                PetBed = 1

                ProceedBuying(" Sucessfully bought 'Pet Bed'!")
        else:
                ProceedBuying(" You don't have enough money! Come back again later.")
    else:
        ERROR("Invalid item (" + str(Item) + ")!")

    return PetFood, PetBed, Pet, Money

def Park():
    global PetHunger
    global PetEnergy
    global Pet

    if Pet == 1:
        WipeScreen(30)
    
        print(" You barely reach out the park's entry and see several dogs are already welcoming you. Unfortunately, they aren't as good doing that.")
        if TipsON == 1:
            print("\n \n   ACTIONS: \n   1.   Abandon your Pet (less money spent) \n   2.   Walk your Pet (increases hunger)")
        else:
            print("\n \n   ACTIONS: \n   1.   Abandon your Pet \n   2.   Walk your Pet") 
    
        Action = int(input("\n What will you do?: "))

        if Action == 1:
            WipeScreen(50)
            print(" LMAO. You really meant that.")

            input("\n \n Press 'enter' to continue reading...")

            WipeScreen(200)
            print("   ~ 2nd SECRET ENDING - CONGRATULATIONS! ~")
            print("   You got out alive and died several decades later, but not your Pet. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")

            SYS.exit()
        elif Action == 2:
            PetEnergy -= Rand.randint(30, 60)
            PetHunger += Rand.randint(20, 40)

            WipeScreen(30)
            print(" " + PetName + " is running wild among the leafy trees and spiky bushes on the forest. The wind it's tail generates makes the scented flowers dance under the mid-morning sun as if happy of the sight.")

            input("\n \n Press 'enter' to continue playing...")

            WipeScreen(50)
            Home()
    else:
        WipeScreen(30)
        print(" YOU: Why'd I go to the park if I do not have any pets?")

        input("\n \n Press 'enter' to continue playing...")
        
        WipeScreen(30)
        Home()

    return PetEnergy, PetHunger, Pet

def NextDay():
    global PetEnergy
    global PetHunger

    global Day

    Day += 1
    
    if Pet == 1:
        if PetBed == 1:
            PetEnergy += (Rand.randint(20, 40))
            PetHunger += (Rand.randint(5, 10))
        else:
            PetEnergy += (Rand.randint(20, 30))
            PetHunger += (Rand.randint(5, 15))
            
    if Day == 32:
        if Pet == 0:
            print("   By the end of the month, both your parents died on an accident. You got depressed and stopped working; you yourself couldn't afford to pay the monthly rent. The landlord brought bandits to your home; they kicked you out and you died out of hunger on the lively streets at night, February " + str(Rand.randint(3, 7)) + ".")

            input("\n \n Press 'enter' to continue reading...")

            WipeScreen(200)
            print("   ~ BAD ENDING - CONGRATULATIONS! ~")
            print("   You got to the end of the month but died after. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")

            SYS.exit()
        else:
            WipeScreen(50)

            print("   By the end of the month, both your parents died on an accident. Luckily, your 'Pet was there, taking care of you itself this time.")

            input("\n \n Press 'enter' to continue reading...")

            WipeScreen(200)
            print("   ~ GOOD ENDING - CONGRATULATIONS! ~")
            print("   You got out alive and died several decades later, together with your Pet. You completed the game on a outstanding manner!; \n   thanks for playing <3 \n \n")

            SYS.exit()
    else:
        print(" It's January " + str(Day) + ".") 
        print(" You have $" + str(Money) + ".")
        print("\n \n   MAP: \n   1. Home \n   2. The Shop \n   3. The Park")

        Place = int(input("\n Where do you want to go?: "))

        if Place == 1:
            Home()
        elif Place == 2:
            Shop()
        elif Place == 3:
            Park()
        else:
            ERROR("Place does not exist (" + str(Place) + ")!")

    return PetEnergy, PetHunger, Day

def FirstDay():
    global TipsON

    print(" It's January 1. You aged 18 yesterday and left home.")

    print("\n \n   OPTIONS: \n   1. Yes \n   2. No")
    BuyPet = int(input("\n Is it a good idea to buy a pet as an attempt to escape loneliness?: "))

    WipeScreen(30)
    print("   OPTIONS: \n   1. Yes \n   2. No (recommended) \n")

    TipsON = int(input(" Play with TIPS on?: "))

    WipeScreen(100)

    if BuyPet == 1:
        print(" It took one whole day for you to take the sole decision of buying a pet. \n")

        NextDay()
    elif BuyPet == 2:
        print(" The thought of buying a pet (or not) assaulted you every often on the day. At the end, you go to bed without doing anything. \n")

        NextDay()
    else:
        ERROR("Invalid action (" + str(Pet) + ")!")

    return TipsON


# === Game === #
FirstDay()
