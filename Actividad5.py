from random import *
from turtle import *
from freegames import path
import time

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

#Definición de la variable en 0
cuadrosDescubiertos = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    
    
    #Definición de variable global de cuadros descubiertos
    global cuadrosDescubiertos
    #Paso 4
    print("Salio el numero: ", tiles[spot])
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    else:
        #Se aumentan los 2 cuadros que se descubrieron en el contador
        cuadrosDescubiertos = cuadrosDescubiertos + 2
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 10, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    #Si los cuadros descubiertos son igual a 64, se detiene el juego y te dice que ganaste
    if(cuadrosDescubiertos == 64):
        spot = index(-80, 1)
        x, y = xy(spot)
        goto(x,y)
        write(" ¡Ganaste!",font=('Arial', 30, 'bold'))
        time.sleep(4)
        exit()
        
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
