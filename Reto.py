# Planteamiento de los 3 ejercisios
# reto unidad tres 

## analisis de los casos 

##1 regulación de la temperatura en el baúl del tren de aterrizaje dependiendo progresivamente de la temperatura de las llantas 
'''
necesitamos controlar la temperatura en las llantas ya que en partes puede ocurrir de que se enfrie demasiado o que se caliente demasiado entonces respecto a esta formula
dT/dt = -k * (T - Te)
dT/dt es la tasa de cambio de temperatura del objeto respecto al tiempo.
k es la constante de enfriamiento o calentamiento, que depende de las propiedades del objeto y del medio en el que se encuentra.
T es la temperatura del objeto en un momento dado.
Te es la temperatura del entorno o medio en el que se encuentra el objeto.
respecto a esto necesitamos que despues del despegue analizar constatntemente cada 10 min la temperatura y corregirla si es necesario
si la temperatura marca un nivel distinto al momento de ejecutar la accion debe mostrar una alerta en cabina respecto a la situacion, y necesitamos
que este estable 5 minutas antes del aterrizaje. en el intervalo de tiempo despues del aterrizaje hasta 5 min antes de aterrizar, la temperatura
de las ruedas este oscilando entre frio o caliente
'''
##2 como segudo caso tenemos la presion dentro de cabina  que varia dependiendo la altitud
'''
En tierra La cabina está igualada con la presión exterior.
Durante el ascenso La presión en cabina empieza a disminuir, pero de forma más lenta que la exterior.
En crucero entre 10.000 y 12.000 m de altura  La cabina suele mantenerse equivalente a estar entre 1.500 y 2.400 m
de altitud aproximadamente 10.9 y 11.6 psi
Durante el descenso  La presión en cabina aumenta suavemente hasta igualar la exterior en el aterrizaje.
'''

##3 como ultimo caso tenemos el medidor de gasolina que es el que nos muestra cuanto nivel tenemos, y si es necesario recargar gaspolina
'''
necesitamos saber cuanto combustibles tiene el avion en vuelo constantemente, y a partir de su distancia, demostrar si si alcanza para el destino propuesto, en caso de 
de que no, hacer un aterrizaje de emergencia 
 '''

'''
1 regulación de la temperatura en el baúl del tren de aterrizaje dependiendo progresivamente de la temperatura de las llantas
Crear una temperatura estable en ela cual se regule la temperatura de el tren de aterrizaje, debido a que el tren de aterrizaje queda con mucho calor despues de el despegue,
necesitas un bucle para poder tener la temperatura de las ruedas estables (ni muy caliente, ni muy fria), la temperatura debe estar cambiando constantemente
para que esten estables, teniedno en cuenta que el baul de el tren de aterrizaje, tambien genera calor y necesita ventilación.
dT/dt = -k * (T - Te) Donde: dT/dt es la tasa de cambio de temperatura del objeto respecto al tiempo. k es la constante de enfriamiento
'''
rn**r-1