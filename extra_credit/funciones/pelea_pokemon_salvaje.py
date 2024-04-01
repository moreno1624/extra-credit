from funciones.ataques import ataques
import random
import os


def pelea(user_in, rival):
    if user_in.pokemon_debilitados == 0:
        while len(user_in.pokemon) != user_in.pokemon_debilitados:
            os.system("cls")
            print("="*55)
            print("pokemones atrapados:\n")
            for pokemon in user_in.pokemon:
                print(f"-{pokemon.nombre}  / vida: {pokemon.vida}\n")
            nombre = input(
                "\nescriba el nombre del pokemon que desea usar\n\t-->")
            print("="*55)
            for poke in user_in.pokemon:
                if poke.nombre == nombre:
                    while poke.vida > 0 and rival.vida > 0:
                        os.system("cls")
                        print("="*55)
                        print(
                            f"\nvida del pokemon oponente: {rival.vida}\n")
                        print(f"vida de tu pokemon: {poke.vida}\n")
                        print("="*55)
                        print("ataques aprendidos:\n")
                        for ataque in poke.ataques:

                            print(f"-{ataque}\n")
                        atack = input("\n que ataque desea usar: ")
                        print("="*55)
                        if atack in poke.ataques:

                            rival, poke = ataques(
                                atack, rival, poke)
                            print(f"\n tu pokemon ha usado {atack}")

                            ataq = random.randrange(
                                0, len(rival.ataques))
                            poke, rival = ataques(
                                rival.ataques[ataq], poke, rival)

                            print(
                                f"\n el pokemon contrario ha usado {rival.ataques[ataq]}")

                            input("\n\tenter para continuar")
                        else:
                            print("\nataque no encontrado intente de nuevo\n")
                            input("enter para continuar")
                    os.system("cls")

                    if poke.vida <= 0 and rival.vida <= 0:

                        print(f"\n{poke.nombre} tuyo se ha debilitado")
                        print(
                            f"\n{rival.nombre} contrario se ha debilitado\n\than quedado empatados\n")
                        user_in.movimientos += 1
                        user_in.pokemon_debilitados += 1
                        return 1

                    elif poke.vida <= 0:

                        print(
                            f"\n{poke.nombre} tuyo se ha debilitado\n\thas perdido\n")
                        user_in.pokemon_debilitados += 1
                        return 2

                    elif rival.vida <= 0:

                        print(
                            f"\n{rival.nombre} contrario se ha debilitado\n\thas ganado\n")
                        user_in.movimientos += 1
                        return 1
                else:
                    print("nombre no encontrado\n")
                    input("\n\tenter para continuar")
    else:
        print(
            "tu pokemon no puede entrar al combate, no tiene suficiente vida\n")
        return 2
