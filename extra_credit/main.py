from funciones.ataques import ataques
from funciones.inicio import inicio
from funciones.orden_all import ubicaciones


def main():
    movimientos = 0
    while True:

        x = input(
            "\nbienvenido, que desea hacer \n\n1-empezar a jugar\n2-salir\n\t-->")
        if x == "1":
            break
        elif x == "2":
            quit()

        else:
            print("\nvalor no valido\n")
            print("="*35)
            continue
    user_in, ubicacion = inicio()
    while ubicacion < 20:
        ubicacion = ubicaciones[ubicacion].show(user_in, ubicacion)
    while ubicacion == 20:
        ubicacion = ubicaciones[ubicacion].liga(user_in, ubicacion)


main()
