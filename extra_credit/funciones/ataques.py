def ataques(input, poke, poke2):
    if input == "ascuas":
        poke.vida -= 30

    elif input == "latigo":
        poke.vida -= 20

    elif input == "hoja afilada":
        poke.vida -= 30

    elif input == "arañazo":
        poke.vida -= 20

    elif input == "lanzallamas":
        poke.vida -= 40

    elif input == "ataque ala":
        poke.vida -= 25

    elif input == "rayo solar":
        poke.vida -= 25

    elif input == "placaje":
        poke.vida -= 15

    elif input == "pistola agua":
        poke.vida -= 40

    elif input == "fortaleza":
        poke2.defensa += 20

    elif input == "electrotela":
        poke.vida -= 20

    elif input == "burbuja":
        poke.vida -= 20

    elif input == "pin misil":
        poke.vida -= 40

    elif input == "ataque rapido":
        poke.vida -= 20
    elif input == "rizo defensa":
        poke.vida -= 15
    elif input == "chirrido":
        poke.vida -= 15

    if poke.defensa <= 0:
        poke.defensa = 1
    if poke2.defensa <= 0:
        poke2.defensa = 1
    return poke, poke2
