from turtle import Screen
from snake import Snake
from food import Food

import time

#Crear escenario
'''
Codigo por segmentos:
snake_segment = Turtle("square")
snake_segment.color('white')
#goto es para mover la serpiente en las diferentes coordenadas
snake_segment2 = Turtle("square")
snake_segment2.color('white')
snake_segment.goto(-20,0)##primer numero es X, segundo número es Y
snake_segment3 = Turtle("square")
snake_segment3.color('white')
snake_segment3.goto(-40,0)
'''
screen = Screen()#se instancia ó crea objeto
screen.setup(width=600, height=600)#metodo setup sale de Screen
screen.bgcolor("black")
screen.title ("Programate snake")

screen.tracer(0)#DESACTIVAR EL EFECTO Animación por defecto

snake = Snake () #crear ó instanciar objeto serpiente

#crear instanciar objeto serpiente
food = Food ()
#Movimientos serpiente
screen.listen()
screen.onkey(snake.up,"Up")#en el parentesis se pone acción y con que rtecla
screen.onkey(snake.down,"Down")#en el parentesis se pone acción y con que rtecla
screen.onkey(snake.left,"Left")#en el parentesis se pone acción y con que rtecla
screen.onkey(snake.right,"Right")#en el parentesis se pone acción y con que rtecla

game_is_on = True ## True y False siempre con mayusculas

while game_is_on:
    screen.update()#refresca la pantalla
    time.sleep(0.2)#para jugar con el tiempo del movimiento de la serpiente

    snake.move()

#cerrar ventana
screen.exitonclick()