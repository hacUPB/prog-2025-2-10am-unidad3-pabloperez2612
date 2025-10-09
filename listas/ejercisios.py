# Lista vacía
componentes = []
import random
elemento = input("ingrese un componente del avion: ")
componentes.append(elemento)
print(componentes)
numeros = []
aleatorio = random.randint(0,100)
numeros.append(aleatorio)
numeros.append(10)

for i in range (10):
    aleatorio = random.randint(0,100)
    aleatorio.append(aleatorio)
print(numeros)

# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Lista con diferentes tipos de datos
datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]



# ejercisio 2

# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):

    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={act}")




#ejercisio 5
'''
generar una lista con 100 numeros aleatorios entre 100 y 1000
calcular el rpomedio de los valores de la lista 
calcular el mayor y menor de los numeros
'''
import random
numeros = []
for i in range (100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)
print(numeros)

suma = 0
for i in range(len(numeros)):
    suma += numeros [i]

prom = suma / len(numeros)
promedio = sum(numeros) / len(numeros)
print (f"promedio = {prom}")

mayor = max( numeros )
menor = min( numeros )
