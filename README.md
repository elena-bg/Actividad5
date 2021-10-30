# Actividad5
Actividad 5. Juego de Memoria

1. Contar y desplegar el numero de taps
  -Para saber cuantos taps se relizaban, se creó una variable contador dentro de la función tap, la cual se tuvo que hacer globl para que esta funcionase de forma correcta, así que cada vez que se hiciera una llamada a la función tap, este contaría uno más y se desplegaría en la consola
2. Detectar cuando todos los cuadros se han destapado
    - Para saber cuando todos los cuadros se destaparon lo que se hizo fue agregar una variable llamada cuadrosDescubiertos y hacerla global dentro de la función de tap, en esta misma función se agregó el sumador para la variable de cuadrosDescubiertos cuando se desvelen 2 cuadros que hayan sido resueltos, luego en la función de draw se agregó un pedazo de código para comprobar cuando se llega a 64 cuadros descubiertos y dice en el centro de la pantalla ¡Ganaste!, espera 4 segundos y se cierra la ventana del juego.
3. Centrar el dígito en el cuadro
    - Para centrar en número en el cuadro, lo que se hizo fue ajustar el punto al que se dirige cuando se le da click al cuadro. Esta instrucción se encuentra en la línea 59 del código, qeu estaba como -goto(x + 2, y)-, y al cambiarlo a -goto(x + 10, y + 5)- el punto se recorre hacia la derecha y hacia arriba y eahí escribe el número a desplegar, que se ve centrado. 
4. Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?
-La mejor manera que se pudo observar para que el jugador tuviese una manera más sencilla de ganar el juego, es si tuviese anotado el número que desplegó, cada que hicisese el tap sobre un recuadro, esto para que el usuario pudiese recordar más facilmente las parejas.
