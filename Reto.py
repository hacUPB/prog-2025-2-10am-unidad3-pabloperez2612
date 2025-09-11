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

