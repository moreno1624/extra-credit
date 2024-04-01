from funciones.registro_perfil import registro_perfil
from clasess.pokemon import Pokemon
from clasess.persona import Persona
from funciones.pelea_personas import pelea
from funciones.curar import curar
import os


def inicio():
    user_in = registro_perfil()
    os.system("cls")
    print("\nOak:  bienvenido al pueblo negro, el pueblo inicial, soy el profesor Oak, te explicare lo que tines que hacer...\n\npor medio de un pokemon que te voy a dar,\nvas a ir a todos los pueblos para vencer a los lideres de gimnasio y coronarte como campeon de la Liga pokemon\n\nde 3 pokemones que tengo te puedo dar 1, piensa un poco antes de elegir ")
    while True:
        print("\nopciones:\n\n-bulbasaur\n\n-charmander\n\n-squirtle\n")
        pokemon = input("cual elijes -->")

        if pokemon == "bulbasaur":

            user_in.pokemon.append(Pokemon("bulbasaur", 100, 100, [
                "latigo", "hoja afilada", "placaje"]))

            rival = Persona("raul", user_in.edad, user_in.lugar_origen, [Pokemon("squirtle", 90, 100, [
                "pistola agua", "burbuja", "placaje"])], 0, 1, 0)
            break

        elif pokemon == "charmander":

            user_in.pokemon.append(Pokemon(
                "charmander", 100, 100, ["arañazo", "ascuas", "lanzallamas"]))

            rival = Persona("raul", user_in.edad, user_in.lugar_origen, [Pokemon("bulbasaur", 90, 100, [
                "latigo", "hoja afilada", "placaje"])], 0, 1, 0)
            break
        elif pokemon == "squirtle":

            user_in.pokemon.append(Pokemon("squirtle", 100, 100, [
                "pistola agua", "burbuja", "placaje"]))
            rival = Persona("raul", user_in.edad, user_in.lugar_origen, [Pokemon(
                "charmander", 90, 100, ["arañazo", "ascuas", "lanzallamas"])], 0, 1, 0)
            break
        else:
            print("valor no valido")
            print("="*35)
            continue
    print("="*35)
    print("\nOak:  sabia eleccion, antes de que empieces tu travesia, hay alguien que me ha dicho que quiere pelear contigo\n\nraul: hola me llamo raul y soy del mismo pueblo que tu, vamos a pelear...\n ")
    input("enter para continuar")
    resultado = pelea(user_in, rival)
    print("="*35)
    print("\nOak: fue una batalla muy reñida, me alegra que entendieran como funcionan las batallas\ncurare sus pokemon para que empiecen cuanto antes su viaje")
    if resultado == 1:
        print("Raul: ... la proxima vez te ganaré, nos encontraremos en la liga pokemon...")
    elif resultado == 2:
        print(
            f"Raul: casi me ganas {user_in.nombre}, entrena a tus pokemon para fortalecerlos y ver tu si me puedes ganar a futuro ")
    elif resultado == 3:
        print("\nRaul: perdi... nos encontraremos despues. definitivamente ganare el siguiente encuentro\n")
    print(f"\noak:{user_in.nombre}, pelea contra otros pokemons para que los tuyos aprendan nuevos ataques y asi hacerte mas fuerte")
    print("="*35)
    user_in = curar(user_in, "Oak")
    return user_in, 0
