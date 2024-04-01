def curar(user_in, name):
    for poke in user_in.pokemon:
        if name == "Oak":
            poke.vida = 100
            poke.defensa = 100
        if name == "pueblo blanco":
            poke.vida = 100
            poke.defensa = 100
        elif name == "pueblo rojo":
            poke.vida = 150
            poke.defensa = 100
        elif name == "pueblo azul":
            poke.vida = 200
            poke.defensa = 100
        elif name == "pueblo amarillo":
            poke.vida = 250
            poke.defensa = 100
        elif name == "pueblo verde":
            poke.vida = 300
            poke.defensa = 100
        elif name == "pueblo marron":
            poke.vida = 450
            poke.defensa = 100
        elif name == "liga":
            poke.vida = 550
            poke.defensa = 100
    user_in.pokemon_debilitados = 0
    print("tu pokes estan curados,vuelve pronto")
    return user_in


def curarlider(user_in, name):
    for poke in user_in.pokemon:
        if name == "pueblo blanco":
            poke.vida = 60
            poke.defensa = 60
        elif name == "pueblo rojo":
            poke.vida = 76
            poke.defensa = 100
        elif name == "pueblo azul":
            poke.vida = 110
            poke.defensa = 100
        elif name == "pueblo amarillo":
            poke.vida = 150
            poke.defensa = 100
        elif name == "pueblo verde":
            poke.vida = 200
            poke.defensa = 100
        elif name == "pueblo marron":
            poke.vida = 250
            poke.defensa = 100
        elif name == "liga":
            poke.vida = 250
            poke.defensa = 80
    user_in.pokemon_debilitados = 0
    return user_in
