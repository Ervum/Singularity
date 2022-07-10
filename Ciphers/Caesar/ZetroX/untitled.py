import string

def cypherText(text, pattern):
    newText = ""
    for char in text:
        if char != " ":
            decimalValue = ord(char.lower()) + pattern
            # Comprobamos si en la tabla ascii se pasa del limite de las minusculas
            if decimalValue > 122:
                decimalValue = decimalValue - 122 + 96 
            elif decimalValue < 97:
                decimalValue = decimalValue + len(string.ascii_lowercase) 
            newChar = chr(decimalValue) if char.islower() else chr(decimalValue).upper() 
            newText += newChar
        else:
            newText += char
    return newText

if __name__ == '__main__':
    text = str(input("Introduce la frase: "))
    pattern = int(input("Introduce la clave: "))

    print( cypherText(text, pattern) )
