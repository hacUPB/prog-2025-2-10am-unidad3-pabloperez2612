numero = int(inout("ingrese el numero de términos de la serie"))
if numero <= 0:
    print("por favor, ingrese un numero entero positivo")
elif numero == 1:
    print("serie de fibonacci")
    print(0)
else:
    a = 0
    b = 1
    contador = 2
    print("serie de fibonacci") 
    print(a)
    print(b)

    while contador < numero :
        siguiente = a + b
        print(siguiente )
        a = b
        b = siguiente
        contador += 1


    
