#Calculadora

control = True #variable booleana
while control == True:
    num1 = int(input("ingrese un  numero"))
    num2 = int(input("ingrese otro numero"))
    print("S. sumar\nR. Restar\nM. multiplicar\nD. Dividir\nP. Potencia\nE. Salir")
    opcion = input("elija una opcion")
    opcion = opcion.upper() ### se convierte el texto en mayusucula
    match opcion:
        case "S":
            print("Suma")
            resultado = num1 + num2
        case "R":
            print("Resta")
            resultado = num1 + num2
        case "M":
            print("multiplicacion")
            resultado = num1 * num2
        case "D":
            print("Division")
            resultado = num1 / num2
        case "P":
            print("Potencia")
            resultado = num1 ** num2
        case "E":
            control = False
        case _:
            print("modo no valido")
    print(f"Resultado = {resultado}")
        