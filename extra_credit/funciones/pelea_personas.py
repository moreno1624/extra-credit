from funciones.ataques import ataques
import random
import os


def pelea(user_in, rival):
    pokemon_rival = 0
    if user_in.pokemon_debilitados == 0:
        if user_in.medallas < rival.medallas:

            while len(user_in.pokemon) != user_in.pokemon_debilitados and len(rival.pokemon) != rival.pokemon_debilitados:
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

                        while poke.vida > 0 and rival.pokemon[pokemon_rival].vida > 0:

                            os.system("cls")
                            print("="*55)
                            print(
                                f"\nvida del pokemon oponente: {rival.pokemon[pokemon_rival].vida}\n")
                            print(f"vida de tu pokemon: {poke.vida}\n")
                            print("="*55)
                            print("ataques aprendidos:\n")
                            for ataque in poke.ataques:

                                print(f"-{ataque}\n")
                            atack = input("\n que ataque desea usar: ")
                            print("="*55)
                            if atack in poke.ataques:

                                rival.pokemon[pokemon_rival], poke = ataques(
                                    atack, rival.pokemon[pokemon_rival], poke)
                                print(f"\n tu pokemon ha usado {atack}")

                                ataq = random.randrange(
                                    0, len(rival.pokemon[pokemon_rival].ataques))
                                poke, rival.pokemon[pokemon_rival] = ataques(
                                    rival.pokemon[pokemon_rival].ataques[ataq], poke, rival.pokemon[pokemon_rival])
                                print(
                                    f"\n el pokemon contrario ha usado {rival.pokemon[pokemon_rival].ataques[ataq]}")
                                input("\n\tenter para continuar")

                            else:
                                print("\nataque no encontrado intente de nuevo\n")
                                input("enter para continuar")

                        os.system("cls")

                        if poke.vida <= 0 and rival.pokemon[pokemon_rival].vida <= 0:

                            print(f"\n{poke.nombre} tuyo se ha debilitado")
                            print(
                                f"\n{rival.pokemon[pokemon_rival].nombre} contrario se ha debilitado")
                            user_in.pokemon_debilitados += 1
                            rival.pokemon_debilitados += 1
                            pokemon_rival += 1

                        elif poke.vida <= 0:

                            print(f"\n{poke.nombre} tuyo se ha debilitado")
                            user_in.pokemon_debilitados += 1

                        elif rival.pokemon[pokemon_rival].vida <= 0:

                            print(
                                f"\n{rival.pokemon[pokemon_rival].nombre} contrario se ha debilitado")
                            rival.pokemon_debilitados += 1
                            pokemon_rival += 1
                    else:
                        print("nombre no encontrado\n")
                        input("\n\tenter para continuar")

            if len(user_in.pokemon) == user_in.pokemon_debilitados and len(rival.pokemon) == rival.pokemon_debilitados:

                print("\n\than quedado empatados\n")
                user_in.movimientos += 1
                return 1

            elif len(user_in.pokemon) == user_in.pokemon_debilitados:

                print("\n\thas perdido\n")
                rival.pokemon_debilitados = 0
                return 2
            elif len(rival.pokemon) == rival.pokemon_debilitados:

                print("\n\thas ganado\n")
                user_in.movimientos += 1
                return 3
        else:
            print("\n\tya venciste a este oponente\n")
    else:
        print(
            "tu pokemon no puede entrar al combate, no tiene suficiente vida\n")
