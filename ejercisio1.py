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

