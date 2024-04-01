from funciones.curar import curar


def pueblo(user_in):
    while True:
        print(f"bienvenido a pueblo negro\n\nopciones:\n1-curar al pokemon\n2-avanzar a la siguiente ubicacion\n")
        op = input("que desea hacer\n\t--->")
        print("="*55)
        if op == "1":
            user_in = curar(user_in, "Oak")
            return user_in
        elif op == "2":
            break
