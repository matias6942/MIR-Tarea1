# MIR-Tarea1

Estas son las instrucciones para ejecutar la Tarea 1 del curso CC5213 - Recuperación de la Información Multimedia.

El objetivo de esta tarea es implementar un detector de comerciales dados un extracto de televisión abierta y ejemplos de comerciales que pueden o no aparecer en el extracto.

## Requerimientos

* Linux
* Python 3.6.6
* OpenCV 3.4.3

## Preparación

Las siguientes carpetas y archivos deben ubicarse dentro del mismo directorio:

* `television` 
* `comerciales`
* `gt.txt`
* `evaluar.py`
* `adsDetector.py`

## Testing

Ejecute el archivo `adsDetector.py`. Se mostrará el siguiente mensaje: 

```
Ingrese el nombre del video de televisión (con su extensión) y luego el nombre de la carpeta con los comerciales a detectar SEPARADOS POR UN ESPACIO:
```
Un ejemplo de input puede ser:

```
mega-2014_04_16.mp4 comerciales
```

Las etapas especificadas en el enunciado de la tarea se irán ejecutando secuencialmente dando aviso por consola.   

Si todo ha salido bien debería ver los siguientes mensajes:
```
I) La extracción de características ha terminado! Los descriptores calculados se encuentran en las carpetas: 

     TelevisionDescriptors y CommercialsDescriptors

 II) La búsqueda por similitud ha terminado! Los conjuntos Q y R se encuentran en la carpeta: 

     SimilaritySearch

 II) La detección de apariciones ha terminado! el resultado se ecuentra en el archivo: 

     detecciones.txt

El tiempo de ejecución fue de: 0:01:52.344613
```

Dependiendo de su hardware, el tiempo de ejecución no debería ser superior a 3 minutos.

## Desarrollo

Esta tarea cuenta con un repositorio de GitHub privado:

    https://github.com/matias6942/MIR-Tarea1

Para solicitar acceso, porfavor escriba a mi correo:

    matias.zamora@ing.uchile.cl






