from funciones.pelea_personas import pelea
from funciones.curar import curar, curarlider
from funciones.pueblo_negro import pueblo
from funciones.moviments import movimientos
import os


class Pueblo:
    def __init__(self, nombre, lider):
        self.nombre = nombre
        self.lider = lider

    def show(self, user_in, ubicacion):
        if len(user_in.pokemon[0].ataques) < 10:
            if user_in.movimientos == 2:
                user_in.movimientos = 0
                user_in = movimientos(user_in)
        while True:
            input("\n\tenter para continuar")
            os.system("cls")
            print("="*55)

            print(f"bienvenido a {self.nombre}\n\nopciones:\n1-luchar contra el lider de gym\n2-curar al pokemon\n3-avanzar a la siguiente ubicacion\n4-retroceder a la anterior ubicacion\n ")
            op = input("que desea hacer\n\t--->")
            print("="*55)
            if op == "1":
                print(
                    f"hola soy {self.lider.nombre} el lider del gym, preparate para luchar\n")
                input("\n\tenter para continuar")
                result = pelea(user_in, self.lider)
                if result == None:
                    pass
                elif result == 1:
                    print(f"{self.lider.nombre}: hemos quedado empatados, pero por tu esfuerzo te dare la medalla. sigue avanzando hacia la liga,has ganado la medalla del {self.nombre}\n")
                    user_in.medallas += 1
                elif result == 2:
                    print(
                        f"{self.lider.nombre}: intentalo de nuevo, te estare esperando")
                    self.lider = curarlider(self.lider, self.nombre)
                elif result == 3:
                    print(
                        f"{self.lider.nombre}: felicidades, has ganado la medalla del {self.nombre}")
                    user_in.medallas += 1
                else:
                    print("valor no valido")

                print("="*55)

            elif op == "2":
                user_in = curar(user_in, self.nombre)
                continue
            elif op == "3":
                if user_in.medallas >= self.lider.medallas:
                    return ubicacion + 1
                else:
                    print("no has vencido al lider del gym para poder avanzar...\n")
                    continue
            elif op == "4":
                if ubicacion == 0:
                    user_in = pueblo(user_in)
                else:
                    return ubicacion - 1

    def liga(self, user_in, ubicacion):

        print("\n\nbienvenido a la liga pokemon...\nesta liga consiste en combates pokemon, desde unas semifinales hasta que se decida el ganador...\nesfuerzate")
        print("="*36)
        input("preciona enter para continuar\n")
        while True:
            self.lider[0] = curarlider(self.lider[0], self.nombre)
            user_in = curar(user_in, self.nombre)
            print(f"\ntu primera batalla sera contra {self.lider[0].nombre}")
            input("preciona enter para continuar")
            result = pelea(user_in, self.lider[0])
            if result == 1:
                user_in = curar(user_in, self.nombre)
                self.lider[0] = curarlider(self.lider[0], self.nombre)
                print("\nse hara el combate nuevamente\n")
                continue
            elif result == 2:
                while True:
                    x = input(
                        "\nque quieres hacer\n1-desafiar la liga de nuevo\n2-salir del juego\n")
                    if x == "1":
                        return ubicacion
                    elif x == "2":
                        quit()
                    else:
                        print("\nvalor no valido\n")
            elif result == 3:
                self.lider[1] = curarlider(self.lider[1], self.nombre)
                user_in = curar(user_in, self.nombre)
                print("\nfelicidades, avanzaras a la gran final\n")

                input("\npreciona enter para continuar")
                while True:
                    print(
                        f"\ntu batalla final sera contra {self.lider[1].nombre}, el lider de la liga")
                    input("\npreciona enter para continuar")
                    result = pelea(user_in, self.lider[1])
                    if result == 1:
                        user_in = curar(user_in, self.nombre)
                        self.lider[1] = curarlider(self.lider[1], self.nombre)
                        print("\nse hara el combate nuevamente\n")
                        continue
                    elif result == 2:
                        while True:
                            x = input(
                                "\nque quieres hacer\n1-desafiar la liga de nuevo\n2-salir del juego\n")
                            if x == "1":
                                return ubicacion
                            elif x == "2":
                                quit()
                            else:
                                print("valor no valido\n")
                    elif result == 3:
                        print(
                            "\nfelicidades, te has coronado como campeon de la liga, has terminado el juego")
                        input("")
                        quit()
