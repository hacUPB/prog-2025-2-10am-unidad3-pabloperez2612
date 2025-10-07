
def primo(numero:int):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1 #cont = cont + 1
    if cont == 2:
        print(f"{numero} es primo")
    else:
        print(f"Los divisores de {numero} son:")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i)
 
def fibonacci(valor:int):
    if valor <= 0:
        print("Por favor, ingrese un número entero positivo.")
    elif valor == 1:
        print("Serie de Fibonacci")
        print(0)
    else:
        a = 0
        b = 1
        contador = 2
        print("Serie de Fibonacci")
        print(a)
        print(b)
       
        while contador < valor:
            siguiente = a + b
            print(siguiente)
            a = b
            b = siguiente
            contador += 1
 
def tabla(numero:int):
    cont = 1
    while cont <= 15:
        res = cont * numero
        print(f"{numero} x {cont} = {res}")
        cont += 1
 
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
tabla(multiplicando)

from src.main import *

def main():

    while True:
        opc = menu()
        match opc:
            case 1:
                print("1. calcula si un numero es primo.")
                valor = int(input("ingresa un n umero mayor que 1>>"))
                primo(valor)
            case 2:
                print("ingrese la serie de fibonacci")
                num = int(input("ingrese el numero de terminos >>"))
                fibonacci(numero)
            case 3:
                print("imprime la tabla de multiplicar")
                num = int(input("ingrese el numero >>"))
                tabla(num)
            case 4:
                break
            case _:
                print("salir")

if __name__ == "__main__":
    main()