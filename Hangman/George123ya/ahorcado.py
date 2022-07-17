import sys
from numpy import random

def menu():
    while True:
        print("\n~~~~~~~~~~~~~~~~~~")
        print("JUEGO DEL AHORCADE")
        print("~~~~~~~~~~~~~~~~~~")
        print("\nElige la categoría de palabra: \n")
        print("  1. Gente\n")
        print("  2. Animales\n")
        print("  3. Alimentos\n")
        print("  4. Dalas\n")
        print("  5. Salir\n")

        categoria = input(" ")
        if categoria.isdigit():
            if int(categoria) in range(1,5):
                break
            elif categoria == "5":
                break
        else:
            print("\n Opción inválida \n")
    return categoria

def choose_word(categoria):
    categorias = {
        "1":["humano", "mujer", "hombre", "niño", "niña", "culo", "dama"],
        "2":["perro", "gato", "conejo", "langosta", "jirafa", "lol", "cucaracha"],
        "3":["castaña", "manzana", "tomate", "sandía", "durazno", "plátano", "pene"],
        "4":["qué asco que das", "dime la definición de psicópata", "¿cómo te quedas?", "wowowowowowow", "me como mi caca"]
        }
    
    numa = random.randint(0,(len(categorias[categoria])-1))
    palabra = categorias[categoria][numa]
    
    return palabra

def show_letras(pseudopalabra, letra, spaces):
    places = []
    countin = 0
    for i in pseudopalabra:
        if i == letra:
            places.append(countin)
        countin += 1
    for place in places:
        spaces = spaces[:place] + letra + spaces[place+1:]

    return spaces

def matar_stickman(pain):
    perder = False
    pain += 1
    if pain == 7:
        perder = True
    return pain, perder

states = [
    "  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n  \n ~~~~~~~~~~~~~~",
    " | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | / \n |/ \n | \n | \n | \n | \n | \n | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | /     | \n |/      | \n | \n | \n | \n | \n | \n | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | /     | \n |/      | \n |     ´___` \n |    ´/° °\` \n |    `\___/´ \n |     `- -´ \n | \n | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | /     | \n |/      | \n |     ´___` \n |    ´/° °\` \n |    `\___/´ \n |     `-|-´ \n |       | \n |       | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | /     | \n |/      | \n |     ´___` \n |    ´/° °\` \n |    `\___/´ \n |     `-|-´ \n |      /|\ \n |       | \n | \n | \n/|\ \n ~~~~~~~~~~~~~~",
    "  _______ \n | /     | \n |/      | \n |     ´___` \n |    ´/x x\` \n |    `\___/´ \n |     `-|-´ \n |      /|\ \n |       | \n |      / \ \n | \n/|\ \n ~~~~~~~~~~~~~~"
    ]

while True:
    category = menu()

    if category == "5" or category == 5:
        break
    else:
        palabra = choose_word(category)
        pseudopalabra = palabra

        tildes = ["á", "é", "í", "ó", "ú"]
        vowels = ["a", "e", "i", "o", "u"]
        for pos in palabra:
                if pos in tildes:
                    pseudopalabra.replace(pos, vowels[tildes.index(pos)])

        spaces = "_"*(len(palabra))
        pain = 0
        perder = False
        letras_usadas = []

        while True:
            print("\n" + states[pain] + "\n")

            if perder:
                print("PERDISTE uwu")
                print("Palabra: " + palabra)
                break

            if spaces == palabra:
                print("GANASTE nwn")
                print("Palabra: " + palabra)
                break

            print(spaces)
            print("\nLetras usadas: " + ', '.join(letras_usadas))
            letra = input("\nLetra que falta: ")

            if letra == "quit":
                break
            elif (len(letra) == 1) and (letra in pseudopalabra):
                spaces = show_letras(pseudopalabra, letra, spaces)
            else:
                pain, perder = matar_stickman(pain)

            letras_usadas.append(letra)
