print("Bienvenid@, jugaremos un juego en el cual solo tienes tres vidas y tienes que adivinar el numero que la PC tiene pensado, el numero sera del 1 al 5:")
print("La PC tambien tiene 3 vidas")
inicio = input("Presione Q para iniciar el juego: ")
inicio.lower()
vidas = 3
vidas_IA = 3
claves = ("Q", "q")
claves_error = ("F", "f")
numeros = 1, 2, 3, 4, 5
while True:
  if inicio not in claves_error:
    break
  elif inicio == "F" or "f":
       print("ERROR, ERROR, ERROR, ERROR")
       sleep(1.5)
       while True:
         jugador_error = int(input("S3LECCEION3 UN NUMMMMER00..(1, 5)::::: "))
         if jugador_error not in numeros:
           print("3RR0R")
           break
         elif jugador_error in numeros:
          ("Modul0 5 (start)")
          print("La PC esta eligiendo")
          IA_error = random.randint(1, 5)
          sleep(2)
          print("La pc a seleccionado " + str(IA_error))
          if str(jugador_error) == str(IA_error):
            print("H4s p3erdido.;.")
            vidas - vidas - 1
            print("tus vidas son " + str(vidas))
            if vidas == 0 or vidas_IA == 0:
              break
          elif str(jugador_error) != str(IA_error):
            print("L4 PC ah p3rdid0")
            vidas_IA = vidas_IA - 1 
            print("V1das d3 la PC " + str(vidas_IA))
            if vidas == 0 or vidas_IA == 0:
              break
        


  
while True:
  if inicio not in claves:
    print("Movimiento no valido")
    break
  elif inicio == "Q" or "q":
    print("Bien comenzemos")
    while True:
      IA = random.randint(1, 5)
      sleep(1)
      print("Listo, la PC ya eligio un numero")
      print("Intenta adivinarlo!!!")
      jugada_player = int(input("seleccione un numero del 1 al 5: "))
      if str(jugada_player) == str(IA):
        print("La PC a perdido!!!")
        vidas_IA = vidas_IA - 1
        print("Vidas de la PC: " + str(vidas_IA))
        if vidas == 0 or vidas_IA == 0:
         print("Juego terminado!!!")
         break
      elif str(jugada_player) != str(IA):
        print("Has perdido :(")
        vidas = vidas - 1
        print("Tus vidas: " + str(vidas))
        if vidas == 0 or vidas_IA == 0:
          print("Juego terminado!!!")
          break
