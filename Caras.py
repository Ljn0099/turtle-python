from time import sleep
from turtle import *
from random import randint
from math import *

shape("turtle")
speed(100)
colormode(255)
pensize(1)
lados = int(input("Introduce el número de lados: "))
avanzar = int(input("Introduce el tamaño de las lineas: "))
multiplicador = int(input("Introduce el tamaño entre lineas: "))
anguloCentral = 360/lados
mirar = 180 / lados + 90
j = 180 / lados
rangoBruto = avanzar / multiplicador
rango = round(rangoBruto)
rango = int(rango)


seth(270)
for i in range(lados): 
    forward(avanzar) 
    backward(avanzar) 
    right(anguloCentral)
    color(randint(0,255), randint(0,255), randint(0,255))

sen = sin(j*pi/180)
ap = 2 * 100 * sen
b = 0

for x in range(rango):
  b = avanzar - x * multiplicador
  ap = 2 * b * sen
  seth(270)
  goto(0,-avanzar+x*multiplicador)
  right(mirar)
  for i in range (lados):
    color(randint(0,255), randint(0,255), randint(0,255))
    forward(ap)
    right(anguloCentral)
    

hideturtle()
sleep(5)