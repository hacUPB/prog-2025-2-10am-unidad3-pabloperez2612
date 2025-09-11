
## ejercisio 1

| Nombre de la variable | dato |    Tipo de variable |   Descripción  |
|---------------------|-------------|-------------------|-----------------|
|   T_min                |Real         |Entrada            |   Límite inferior permitido de temperatura.|
|T_max                |Real         |Entrada            |   Límite superior permitido de temperatura.|
|intervalo            |Entero       |Entrada            |   Tiempo entre monitoreos de temperatura (en minutos).|
|tiempo_vuelo         |Entero       |Entrada            |Duración total del vuelo.|
|T_actual             |Real         |Control            |Temperatura actual de una llanta en un momento dado.|
|tiempo_actual        |Entero       |Control            |Tiempo transcurrido desde el despegue.|
|dT_dt                |Real         |Control            |Tasa de cambio de temperatura calculada.|
|T_nueva              |Real         |Control            |Temperatura después de aplicar corrección.
|tiempo_estabilizacion|Entero       |Control            |Tiempo antes del aterrizaje en el que la temperatura debe estar estable.|
|tiempo_inicio_estabilizacion|Entero|Control            |Tiempo donde inicia la fase crítica antes del aterrizaje.|
|mostrarAlerta(mensaje)|Función / salida|Salida         |Función que alerta en cabina si la temperatura no está en el rango esperado.|
|RegistrarTemperatura(t, T)|Función / salida|Salida     |Función que guarda las temperaturas monitoreadas.|
|corregirTemperatura()|Función / salida|Salida          |Acción correctiva ejecutada para ajustar la temperatura.|
|Te                   |Real         |constante          |Temperatura landing gear bay (cabina del tren de aterrizaje).|
|k                    | 5, 8, 10  |constante            |   Constante de enfriamiento/calentamiento de la formula respecto al avion  |
|intervalo            | entero   |salida          |   Tiempo entre monitoreos de temperatura (en minutos).|

## ejercisio 2

## 2 problema
|Nombre de la variable  |	Tipo de dato|	Tipo de variable|	Descripción|
|-------------------    |-------------  |-------------------|--------------|
|altitud                | entero        |entrada            |altura en tierra, en vuelo|
|presion_cabina         |entero         |constante          |es la presion que siempre debe tener dentro de la cabina |
|presion_exterior       |entero         |entrada            |es la presion atmosferica por fuera de cabina en vuelo y en tierra|
|presion                |entero         | control           |presion que tiene que disminuir o aumentar dependiendo de la altitud para garantizar la presion en cabina|
|mensaje                |txto           |salida             |es la que le muestra al piloto si la cabina esta bien presurizada o toca hacerle algun cambio|
|presion_maxima         | real          | constante         |no debe pasarse de 11.10 psi|
|presion_minima         | real          |constante          |no debe rebajarse de 10.9 psi|