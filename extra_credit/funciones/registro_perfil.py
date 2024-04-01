from clasess.persona import Persona


def registro_perfil():
    nombre = input("\ningrese su nombre \t-->")
    edad = input("ingrese su edad \t-->")
    while not edad.isnumeric():
        edad = input("error/ ingrese su edad \t-->")
    lugar = input("ingrese su lugar de origen \t-->")
    print("="*55)
    return Persona(nombre, edad, lugar, [], 0, 0, 0)
