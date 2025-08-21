nombre = input("ingresa tu nombre y apellido")
#opcion 1
print("Bienvenidos: ")
print (nombre)
#opcion 2
print("Bienvenidos: ",nombre)
#Calcular indice de masa corporal de una persona
## leer peso, altura
peso= input ("ingresa tu peso en kg")
altura = input ("ingresa tu talla en metros: ")
peso = float(peso)         
altura = float(altura)
#Calculos
imc = peso/altura**2
#mostrar imc
print ("tu imc =", imc)
if imc > 18.5 and imc < 24.9 :
    print("su peso es normal")
else:
    if imc > 25 and imc < 29.9 :
        print("tiene sobrepeso")
    else:
        if imc > 30 and imc < 34.4 :
            print("tiene obesisdad1")
        else:
            if imc > 35 and imc < 39.9 :
                print ("tiene obesidad 2")
            else:
                print("tienes obesidad extrema")
                
    
