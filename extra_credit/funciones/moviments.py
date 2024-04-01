ataques = ["ascuas", "latigo", "hoja afilada", "arañazo", "lanzallamas", "ataque ala", "rayo solar",
           "placaje", "pistola agua", "fortaleza", "burbuja", "pin misil", "ataque rapido", "rizo defensa", "chirrido"]


def movimientos(user_in):
    print("\ntu pokemon puede ganar un nuevo ataque\n elije sabiamente\n")
    while True:
        for ataque in ataques:
            if ataque not in user_in.pokemon[0].ataques:
                print(f"-{ataque}")
        new = input("\nescribe el ataque que quieres\n\t-->")
        if new in ataques and new not in user_in.pokemon[0].ataques:
            user_in.pokemon[0].ataques.append(new)
            return user_in
        else:
            print("valor no valido intentelo de nuevo\n")
            print("="*44)
