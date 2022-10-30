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
speed(6)


for i in range(8): 
    forward(100) 
    backward(100) 
    right(45)

sen = 0.3826834323650897717284599840304
ap = 2 * 100 * sen
b = 0

seth(270)
goto(0,-100)
right(112.5)
for i in range (8):
  forward(2 * 100 * sen)
  right(45)


for x in range(19):
  b = 95 - x * 5
  ap = 2 * b * sen
  seth(270)
  goto(0,-95+x*5)
  right(112.5)
  for i in range (8):
    forward(ap)
    right(45)

hideturtle()
sleep(5)