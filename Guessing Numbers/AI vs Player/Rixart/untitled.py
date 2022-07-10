import random
import os

numero_bajo = 1
numero_alto = 100
SECRET_NUM = random.randint(numero_bajo, numero_alto)

user_num = 1
left = 1

machine_num = 100
right = 100

print(f'El que primero adivine el número entre {numero_bajo}-{numero_alto} gana!\n'.center(120))
while True:
    user_num = int(input(f"Adivina el número. Está entre {left}-{right}\n"))

    if user_num != SECRET_NUM:
        # Se sale de rango
        if user_num > right or user_num < left:
            print(f"\n¡FUERA DE RANGO!:no_entry_sign:\nEl rango es: {left}-{right}\n")
        # Se pasa del VALOR SECRETO
        elif user_num > SECRET_NUM:
            right = user_num
        # sea menor del VALOR SECRETO. CASO NORMAL
        else:
            left = user_num
    else:
        print(f"El usuario ganó:man:\nEl número era el {user_num}")
        break

    machine_num = random.randint(left, right)  # generación del número de la maquina
    print(f":robot: Maquina seleccionó el {machine_num} entre {left}-{right}")

    if machine_num != SECRET_NUM:
        # El valor de maquina es menor que VALOR SECRETO
        if machine_num < SECRET_NUM:
            left = machine_num

        # Sea mayor que el valor secreto CASO NORMAL:
        else:
            right = machine_num
    else:
        print(f"La maquina ganó:desktop:\nEl número era el {machine_num}")
        break

    input("\nEnter para pasar a la siguiente ronda...")
    os.system("clear")
