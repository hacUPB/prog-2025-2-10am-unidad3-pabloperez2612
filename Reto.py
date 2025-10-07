# Codigos 


## ejercisio 2


Factor_de_ajuste = 0.0004
Presion_maxima = 18
Presion_minima = 14

altitud_inicial = float(input("Ingrese la altitud inicial: "))
altitud_crucero = float(input("Ingrese la altitud de crucero : "))
presion_exterior = float(input("Ingrese la presión exterior inicial: "))

presion_cabina_actual = presion_exterior
print("Simulación iniciada")
print("Presión de cabina inicial igualada a la presión exterior.")

altitud = altitud_inicial
subiendo = True
                       3

while True:
    if subiendo:
        if altitud < altitud_crucero:
            altitud += 500
            if altitud > altitud_crucero:
                altitud = altitud_crucero
        else:
            subiendo = False
  
    else:
        if altitud > 0:
            altitud -= 500
            if altitud < 0:
                altitud = 0
        else:
            break  

    if altitud <= 10000:
        presion_objetivo = presion_exterior + (altitud * Factor_de_ajuste)
        mensaje = "Ajustando presión de cabina."
    elif 10000 < altitud <= 12000:
        presion_objetivo = 15
        mensaje = "Manteniendo presión de cabina en crucero."
    else:
        presion_objetivo = presion_exterior - (altitud * Factor_de_ajuste)
        mensaje = "Ajustando presión de cabina."

    presion_cabina_actual = presion_objetivo

    if presion_cabina_actual > Presion_maxima:
        presion_cabina_actual -= 0.3
        mensaje += " Exceso de presión"
    elif presion_cabina_actual < Presion_minima:
        presion_cabina_actual += 0.3
        mensaje += " Baja presión"
    else:
        mensaje += "Presión de cabina óptima"

    print(f"Altitud: {altitud:.1f} m , Presión Cabina: {presion_cabina_actual:.2f} psi , Estado: {mensaje}")


if presion_cabina_actual != presion_exterior:
    presion_cabina_actual = presion_exterior
    mensaje = "Avión en tierra"
else:
    mensaje = "Avión en tierra."

print("\nAterrizaje completado")
print(f"Estado final: {mensaje}, Presión final: {presion_cabina_actual:.2f} psi")

## ejercisio 1

Te_inicial = float(input("Ingrese la temperatura inicial (°C): "))
tiempo_vuelo = float(input("Ingrese el tiempo de vuelo (minutos): "))

Te_min = 30  
Te_max = 80  
intervalo_1 = 10  
tiempo_estabilizacion = 5  
Te_actual = Te_inicial
intervalo_2 = 2  

print("1. Boeing 747-8 (k = 5)")
print("2. Airbus A380-800 (k = 8)")
print("3. Antonov An-225 (k = 10)")      
   
opcion = int(input("Seleccione el avión: "))
  
match opcion:
    case 1:
        print("1. Boeing 747-8 (k = 5)")
        k = 5
    case 2:
        print("2. Airbus A380-800 (k = 8)")
        k = 8
    case 3:
        print("3. Antonov An-225 (k = 10)")
        k = 10
    case _:
        print("Opción no válida")
    

tiempo_inicio_estabilizacion = tiempo_vuelo - tiempo_estabilizacion
tiempo_actual = 0
while tiempo_actual < tiempo_vuelo:
    tiempo_actual += intervalo_1

   
    dT_dt = -k * (Te_actual - Te_inicial)
    Te_nueva = Te_actual + (dT_dt * (intervalo_1 / 60))  

    Te_actual = Te_nueva
                                                       #este condicional nos lo ayudo la IA
    if tiempo_actual < tiempo_inicio_estabilizacion:
        if (int(tiempo_actual / intervalo_1)) % 2 == 0:
            Te_actual += 3  
        else:
            Te_actual -= 3  

        
    if Te_actual < Te_max:
        print("La temperatura del LG es menor que la temperatura máxima, verificar si es menor que la mínima")
        if Te_actual < Te_min:
            print("Cuidado: temperatura muy fría")
            Te_actual += (-k * (Te_actual - Te_inicial)) * (intervalo_2 / 60)
        else:
            print("Temperatura en rango ideal")
    else:
        print("temperatura muy caliente")
        Te_actual -= (-k * (Te_actual - Te_inicial)) * (intervalo_2 / 60)

    if tiempo_actual >= tiempo_inicio_estabilizacion:
        print("Fase de estabilización, asegurar para aterrizar")
    else:
        print("No iniciar fase de estabilización, seguir monitoreando.")

    print(f"Temperatura actual: {Te_actual:.2f} °C")