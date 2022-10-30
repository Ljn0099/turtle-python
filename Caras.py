from time import sleep
from turtle import *
from random import randint
from math import *

#t.forward(pasos) == Ir hacia alante
#t.backward(pasos) == Ir hacia atras
#t.left(grados) == Ir hacia la izquierda
#t.right(grados) == Ir hacia la derecha
#t.goto(x,y) == Ir a
#t.circle(radio) == Hacer circulo
#t.dot(tamaño) == hacer un punto
#t.pensize(tamaño) == cambiar trazo
#t.pencolor("color") == cambiar color
#t.speed(velocidad) == cambiar velocidad
#t.fillcolor("color") == color a rellenar
#t.begin_fill() == empezar rellenado
#t.end_fill() == terminar rellenado
#t.penup() == dejar de escibir
#t.pendown() == volver a escribir



shape("turtle")
speed(100)
colormode(255)
pensize(1)
lados = 13
anguloCentral = 360/lados
mirar = 180 / lados + 90
j = 180 / lados

seth(270)
for i in range(lados): 
    forward(100) 
    backward(100) 
    right(anguloCentral)
    color(randint(0,255), randint(0,255), randint(0,255))

sen = sin(j*pi/180)
ap = 2 * 100 * sen
b = 0

seth(270)
goto(0,-100)
right(mirar)
for i in range (lados):
  forward(2 * 100 * sen)
  right(anguloCentral)
  color(randint(0,255), randint(0,255), randint(0,255))


for x in range(19):
  b = 95 - x * 5
  ap = 2 * b * sen
  seth(270)
  goto(0,-95+x*5)
  right(mirar)
  for i in range (lados):
    color(randint(0,255), randint(0,255), randint(0,255))
    forward(ap)
    right(anguloCentral)
    

hideturtle()
sleep(5)