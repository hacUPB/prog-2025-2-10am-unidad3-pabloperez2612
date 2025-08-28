# 2 ejercisios (uno con condicional dobles y otro con simple)

## Ejercisio de condicional simple
Una escuela requiere determinado numero de computadores, la empresa que los vende condiciona que si el colegio pide 200 o menos computadores cobrar impuesto a cada computador del 20%, en caso de que sean mas de 200 computadores, no cobrar impuesto, cada computador cuesta 2000000

## ejercisio condicional doble
una empresa de vaporizadores, vende vaporizadores al por mayor, en caso de que el numero que solicite el comprador sea menor a 20 cada vaporizador se le compra a 20.000, si son mas de 20 vaporizadores solicitados, cada vaporizador tendria un precio de 18.000

##ejercisio propuesto por compañero
se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.
numero = int(input("ingrese un numero entero"))
residuo = (numero % 3)
print(numero % 3)
if residuo = 0 :
    print (f"{numero} es divisible entre 3")

## matchopcion = input("seleccion una opcion: ")


opcion = int(input("Selecciona una opción: "))

match opcion:
    case "A":
        print("Mostrando datos de sensores...")
    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
