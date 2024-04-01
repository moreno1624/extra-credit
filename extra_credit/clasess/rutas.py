import os
from funciones.pueblo_negro import pueblo
from funciones.pelea_pokemon_salvaje import pelea
from funciones.moviments import movimientos
import random


class Rutas:
    def __init__(self, nombre, pokemon_salvaje):
        self.nombre = nombre
        self.pokemon_salvaje = pokemon_salvaje

    def show(self, user_in, ubicacion):
        if len(user_in.pokemon[0].ataques) < 10:
            if user_in.movimientos == 2:
                user_in.movimientos = 0
                user_in = movimientos(user_in)
        while True:
            input("\n\tenter para continuar")
            os.system("cls")
            print("="*55)
            print(
                f"bienvenido a {self.nombre}\n\nopciones:\n1-avanzar a la siguiente ubicacion\n2-retroceder a la anterior ubicacion\n ")
            op = input("que desea hacer\n\t--->")
            print("="*55)
            if op == "1":
                if self.pokemon_salvaje.vida > 0:
                    x = random.randrange(1, 3)
                else:
                    x = 2
                if x == 1:
                    print(
                        f"te has encontrado a un {self.pokemon_salvaje.nombre}\n")
                    input("\n\tpresione enter")
                    result = pelea(user_in, self.pokemon_salvaje)
                    if result == 1:
                        return ubicacion+1
                    else:
                        continue

                else:
                    return ubicacion+1

            elif op == "2":
                if ubicacion == 0:
                    user_in = pueblo(user_in)
                else:
                    return ubicacion - 1
            else:
                print("valor no valido")
