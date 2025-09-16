##Range: secuencia de numeros. cont (valor de los numeros)
'''
for cont in range(5, 20, 1):
    print(cont)
    '''

## ejercisio 1
#Escribe un programa que solicite al usuario ingresar un número entero positivo n.
#Luego, utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n.
  #  Finalmente, muestra el resultado de la suma en pantalla.


numero = int(input("ingrese un numero entero positivo"))
acum = 0
for cont in range (1, numero+1,):
    if cont % 2 == 0:
        acum += cont 
print(f"La suma de los números pares desde 1 hasta {numero} es: {acum}")
acum += 1

## ejercisio 2
mensaje = "universidad Pontificia Bolivariana"
numero = int(input("ingrese el numero positivo"))
for i in range (numero):
    print(mensaje)