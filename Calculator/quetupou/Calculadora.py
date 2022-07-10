#QUETUPOU | CALCULADORA

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def activar():
    entrada = input("Puedes sumar, restar, dividir o multiplicar. ¿Cuál es tu operación?:_")
    entradaf1 = entrada.replace("x", "*").replace("·", "*").replace("×", "*")
    entradaf2 = entrada.replace(":", "/").replace("÷", "/").replace(" ", "")
    si = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "(", ")", "+", "-", "/")
    for i in range(len(entradaf2)):
        for e in range(len(si)):
            if str(entradaf2[i]) == si[e]: print("El carácter " + entradaf2[i] + " es válido")
            else: print(bcolors.FAIL + "El carácter " + entradaf2[i] + " es inválido" + bcolors.OK)
    activar()


def aritmetica(a, o, b):
    if o == "+": return a + b
    if o == "-": return a-b
    if o == "/": return a/b
    if o == "*": return a*b

    
activar()
