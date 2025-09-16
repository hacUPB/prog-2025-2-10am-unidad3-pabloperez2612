numero=1
while numero <= 99:
    print(numero)
    numero += 2
##2
numero = 100
while numero >= 0:
    print(numero)
    numero -= 5
##3
### solicitar 2 numeros al usuario e imprimir los pares entre ellos
numero_1 = int(input("ingrese un  numero"))
numero_2 = int(input("ingrese otro numero"))
if numero_1 > numero_2:
    mayor = numero_1
    menor = numero_2
else:
    mayor = numero_2
    menor = numero_1
'''
while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
        menor += 1
'''
'''
if menor % 2 == 1:
    menor += 1
while menor <= mayor:
    print(menor)
    menor += 2
'''






