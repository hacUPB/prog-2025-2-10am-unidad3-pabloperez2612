
'''
variables de entrada
nombre             Ripo
opcion             str
tipo               float

Variables de salida
nombre             Tipo
conversion         Float

Variable de control
opcion
'''

opcion = "Z" ### se le asigna el valor a z, para que entre de una vez al while
while opcion != "Q" :
    opcion = input("F. Farenheit a Celsius\nC. Celsius  a Farenheit\nQ. Salir\n")
    opcion = opcion.upper()
    if opcion != "Q" :
        temperatura = float(input("ingrese la temeratura a convertir: "))
        match opcion:
            case "F":
                conversion = (temperatura - 32) * (5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case "C":
                conversion = (temperatura * 9/5) + 32
                print(f"{temperatura}°C = {conversion}°F")
            case _:
                print("opcion no valida")
    else:
        print("saliendo del programa")


