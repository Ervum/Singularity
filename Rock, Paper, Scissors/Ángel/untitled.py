import random 

def juego_simple():

     while True:
      opciones = ("papel", "tijeras", "piedra")
      print("hoy vamos a jugar piedra, papel o tijera ")
      Tu_eleccion = input("pon tu opcion aqui -> ").lower()
      eleccion_ia = random.choice(opciones)
      print ("La eleccion de la Ia es " + eleccion_ia )
      if Tu_eleccion == eleccion_ia:
                print("Empate") 
      elif Tu_eleccion != eleccion_ia and Tu_eleccion == "piedra" and eleccion_ia == "tijeras":
                 print("Tu ganas")
      elif Tu_eleccion == "piedra" and eleccion_ia == "papel":
                 print("Tu pierdes")
      elif Tu_eleccion == "papel" and eleccion_ia == "tijeras":
                 print("Tu pierdes")
      elif  Tu_eleccion == "papel" and eleccion_ia == "piedra":
                 print("Tu ganas") 
      elif Tu_eleccion == "tijeras" and eleccion_ia == "piedra":
                 print("Tu pierdes") 
      elif Tu_eleccion == "tijeras" and eleccion_ia == "papel":
                 print("Tu ganas")


juego_simple()
