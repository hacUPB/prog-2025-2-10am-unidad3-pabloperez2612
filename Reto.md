# Planteamiento de los 3 ejercisios
# reto unidad tres 

## analisis de los casos 

##1 regulación de la temperatura en el baúl del tren de aterrizaje dependiendo progresivamente de la temperatura de las llantas 
'''
necesitamos controlar la temperatura en las llantas durante el vuelo debido a que despues del despegue, las ruedas del avión
quedan muy calientes debido a la fricción de la pista, durante el vuelo, la temperatura de refrigeracion del compartimiento del tren de aterrizaje
va a estar cambiando cada 5 minutos para que la temperatura de las ruedas este oscilando, con esta formula,
vamos a poder definir cuanta temperatura puede cambiar (aumentar o disminuir) con respecto a la temperatura del tren de aterrizaje despues del despegue
dT/dt = -k * (T - Te)
dT/dt es la tasa de cambio de temperatura del objeto respecto al tiempo.
k es la constante de enfriamiento o calentamiento, que depende de las propiedades del objeto y del medio en el que se encuentra.
T es la temperatura del objeto en un momento dado.
Te es la temperatura del entorno o medio en el que se encuentra el objeto.
la constante k solo tendra 3 valores propuedos respecto a los aviones
k para el Airbus A380-800 = 8
k para  el Boeing 747-8 = 5
k para el Antonov An-225 = 10
respecto a esto necesitamos corregirla
en caso de que la temperatura sobre pase un limite por las oscilaciones ( demasiado bajo o demasiado alto) ordenar al piloto active el sistema de refrigeración controlado, en el cual el piloto podra escoger
las temperaturas ideales del sistema de refrigeracion para que enfrie o caliente con mayor intensidad. en caso de activar este sistema, se mostrará un mensaje con las regulaciones ideales
debido a que si el tren de aterrizaje esta muy frio, no puede recibir una temperatura muy caliente en el instante, o si esta muy caliente, no puede recibir una temperatura muy fria por parte del sistema de refrigeracion
regulado, debido a que se puede dañar el caucho de las ruedas del tren de aterrizaje, en caso de que se escoja una temperatura ideal que lo dañe, mostrar un error y el piloto debera escoger otra temperatura ideal
que este estable 10 minutas antes del aterrizaje. en el intervalo de tiempo despues del aterrizaje hasta 5 min antes de aterrizar, la temperatura
de las ruedas este oscilando entre frio o caliente
finalizar 10 min antes del aterrizaje, cuando ya la tempoeratura de las ruedas esten estables.
'''
##2 como segudo caso tenemos la presion dentro de cabina  que varia dependiendo la altitud
'''
En tierra La cabina está igualada con la presión exterior.
Durante el ascenso La presión en cabina empieza a disminuir, pero de forma más lenta que la exterior.
En crucero entre 10.000 y 12.000 m de altura  La cabina suele mantenerse equivalente a estar entre 1.500 y 2.400 m
de altitud aproximadamente 10.9 y 11.6 psi
Durante el descenso  La presión en cabina aumenta suavemente hasta igualar la exterior en el aterrizaje.
En este caso debemos calcular constantemente una regulación del aire y de presión en cabuina para que la misma se mantenga presurizada
y pueda resitir la presión exterior.
'''

## pseudocodigo 1
´´´  
Inicio  
leer Te_inicial,tiempo_vuelo       
Te_min = 30 "grados celsius"    
Te_max = 80 "grados celsius"    
K = constante de enfriamiento   
Intervalo_1 = 10 "minutos"     
tiempo_estabilizacion = 5 "minutos"    
Te_actual = Te_inicial        
intervalo_2 = 2 "minutos"   
mostrar ("1. Boeing 747-8 (k = 5)\n2. Airbus A380-800 (k = 8)\n3. Antonov An-225(k = 10)")
leer opcion :
    si opcion 1. avion 1:
    |   Imprimir "1. Boeing 747-8 (k = 5)"
    |   k = 5
    fin si
    si opcion 2. avion 2:
    |   Imprimir "2. Airbus A380-800 (k = 8)"
    |   k = 8
    fin si
    si opcion 3. avion 3:
    |   Imprimir "3. Antonov An-225(k = 10)"
    |   k = 10
    fin si 
    si opcion 4. avion no es valido :
    |   Imprimir "Opción no válida"
    fin si 
fin opcion

tiempo_inicio_estabilizacion = tiempo_vuelo - tiempo_estabilizacion 
tiempo_actual = 0
Mientras  tiempo_actual < tiempo_inicio_estabilizacion
    
    tiempo_actual = tiempo_actual + intervalo_1
   
    dT_dt = -k * (Te_actual - Te)
    Te_nueva = Te_actual + (dT_dt * intervalo_1)
   
    Te_actual = Te_nueva
    
    SI tiempo_actual < tiempo_inicio_estabilizacion ENTONCES   "hecho IA"
        SI (tiempo_actual / intervalo) MOD 2 = 0 ENTONCES
            T_nueva = T_nueva + 3    // sube (caliente)
        SINO
             T_nueva = T_nueva - 3    // baja (frío)
        FIN SI
    FIN SI

    si Te_max > Te_actual :
        mostrar (" la temperatura del lg es menor que la temperatura maxima, verificar si es menor que la minima")
        si Te_min > Te_actual :
            mostrar ("cuidado temperatura muy fria")
            Te_actual = Te_actual + (dT_dt )* (intervalo_2 / 60)
            si no :
                mostrar (" temperatura en rango ideal")
        fin si
    si no : 
        mostrar (" cuidado temperarura muy caliente ")
        Te_actual = Te_actual - (dT_dt) * (intervalo_2 / 60)
    fin si
    si tiempo_actual >= tiempo_inicio_estabilizacion :
        mostrar ("Fase de estabilizacion, Asegurar temperatura estable para el aterrizaje.")
    si no :
        mostrar ("no iniciar fase de estabilizacion, seguir monitoreando")
    fin si
    mostrar te_actual
        imprimir ("temperatura actual")
FIN MIENTRAS


FIN
´´´´
## pseudocodigo 2


´´
Inicio

Factor_de_ajuste = 0.0004  
Presion_Maxima = 18
Presion_Minima = 14

mostrar  "Ingrese la altitud inicial: "
Leer altitud_inicial

mostrar "Ingrese la altitud de crucero: "
Leer altitud_crucero

mostrar "Ingrese la presión exterior inicial: "
Leer presion_exterior

presion_cabina_actual ← presion_exterior
mostrar "Simulación iniciada"
mostrar "Presión de cabina inicial igualada a la presión exterior."

altitud = altitud_inicial
subiendo = VERDADERO

Mientras verdadero hacer
    si subiendo entonces
        si altitud < altitud_crucero entonces
            altitud = altitud + 500
            si altitud > altitud_crucero entonces
                altitud = altitud_crucero
            fin si
        sino
            subiendo = FALSO
        fin si
    sino
        si altitud > 0 entonces
            altitud = altitud - 500
            si altitud < 0 entonces
                altitud = 0
            fin si
        sino
            salir del ciclo
        fin si
    fin si

    si altitud <= 10000 entonces
        presion_objetivo = presion_exterior + (altitud * FACTOR_DE_AJUSTE)
        mensaje = "Ajustando presión de cabina."
    sino si altitud > 10000 y altitud <= 12000 entonces
        presion_objetivo = 15
        mensaje = "Manteniendo presión de cabina en crucero."
    sino
        presion_objetivo = presion_exterior - (altitud * FACTOR_DE_AJUSTE)
        mensaje = "Ajustando presión de cabina."
    fin si

    presion_cabina_actual = presion_objetivo

    si presion_cabina_actual > PRESION_MAXIMA entonces
        presion_cabina_actual = presion_cabina_actual - 0.3
        mensaje = mensaje + " Exceso de presión"
    sino si presion_cabina_actual < PRESION_MINIMA entonces
        presion_cabina_actual = presion_cabina_actual + 0.3
        mensaje = mensaje + " Baja presión"
    sino
        mensaje = mensaje + " Presión de cabina óptima"
    fin si

    mostrar "Altitud:  {altitud}m , Presión Cabina: {presion_cabina_actual} psi , Estado: {mensaje}"

fin mientras

si presion_cabina_actual ≠ presion_exterior entonces
    presion_cabina_actual = presion_exterior
    mensaje = "Avión en tierra"
sino
    mensaje = "Avión en tierra."
fin si

mostrar "Aterrizaje completado"
mostrar "Estado final: ", {mensaje}, " Presión final: ", {presion_cabina_actual}, " psi"

fin
´´´´

## modificaciones lista, diccionario

### lista
vamos a hacer lista en la cual vamos a encontrar los datos generados por el bucle

### diccionario
en el diccionario vamos a agregar los paramatetros necesarios en el codigo
-