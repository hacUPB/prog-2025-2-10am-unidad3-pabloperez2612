#determinar si un numero es par o impar
numero = int(input("ingrese un numero entero"))
residuo = numero % 2
##Si residuo es 0, es un numero par
if residuo == 0:
    print(numero, " es par")
##Si no es, impar
else:
    print(numero," es impar")