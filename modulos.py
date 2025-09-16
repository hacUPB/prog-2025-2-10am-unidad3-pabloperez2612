import fun_primo_fibonacci_tabla
#Funcion principal
numero = int(input("Ingrese un número entero mayor que 1: "))
fun_primo_fibonacci_tabla.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
fun_primo_fibonacci_tabla.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
fun_primo_fibonacci_tabla.tabla(multiplicando)
´´´
from fun_primo_fibonacci_tabla import *  ##es para importar todo (el * significa todo)

primo(456)
tabla(9)
fibonacci(8)

def menu():
    print("1. Numero primo")
    print("2. serie de fibonacci")
    print("tabala de multiplicar")
    print("4. salir")
