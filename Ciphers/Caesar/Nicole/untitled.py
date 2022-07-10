def setKey(abc):
    print(len(abc))

    print("Ingrese la llave que correspondería a la palabra 'pambisito' con tu propio cifrado cesar (no es necesaria la palabra entera): ")
    llave = str(input(""))

    patron = 0
    for i in range(len(abc)):
        if(llave[0]==abc[i]):
            patron = i-15
            break

    print("El patron es "+str(patron)+" la letra 'p' corresponde a "+str(abc[15+patron]))
    return patron

def translate(patron, abc, texto):
    translated = ""
    for i in range(len(texto)):
        toAdd = ''
        if(texto[i]==' '):
            toAdd = ' '
        else:
            try:
                num = ((abc.index(texto[i]))-(patron))
                if(num>26):
                    num = num-25
                toAdd = abc[num]
            except ValueError:
                toAdd = '0'
        translated = translated+str(toAdd)
    return translated

if __name__ == '__main__':
    abc = list(map(chr, range(97, 123)))
    patron = setKey(abc)
    using = True

    while(using):
        text = (input("Ingrese el texto que desee traducir ('quit' para salir/'reset' para reestablecer la llave): ")).lower()
        if(text=="quit"):
            using = False
        elif(text=="reset"):
            patron = setKey(abc)
        else:
            print(translate(patron, abc, text))
