from tkinter import LEFT, RIGHT
from turtle import  Turtle

from requests import head

    #tuplas = COORDENADAS
STARTING_POSITION = [(0,0),(-20,0), (-40,0)]#constante se crea siempre con mayusculas

#CONSTANTES PARA LOS MOVIMIENTOS
UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0


# creación del cuerpo de la serpiente
class Snake:

    def __init__(self):  #crear el constructor
        self.segments = []#atributo para guardar los segmentos
        self.create_snake()#metodo encargado de crear la serpiente:
        self.head = self.segments[0]#nuevo atributo para almacenad la cabeza, se guarda en una variable

    def create_snake(self): #creación de método
        #Codigo con ciclo FOR
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self, position):
            snake_segment = Turtle("square")
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position)##primer numero es X, segundo número es Y
            self.segments.append(snake_segment) #agregar elementos a la lista self.segments

    def extend(self):#hacer crecer la serpiente
        self.add_segment(self.segments[-1].position())


    #metodo movimiento de la 
    def move(self):
        for seg_num in range(len(self.segments) -1, 0,-1):
            new_x=self.segments[seg_num - 1].xcor()
            new_y=self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)
        #segments[0].left(90)

    def up(self):#metodo para tecla up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):#metodo para tecla down
          if self.head.heading() != UP:
             self.head.setheading(DOWN)
    
    def left(self):#metodo para tecla left
          if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)
    
    def right(self):#metodo para tecla right
          if self.head.heading() != LEFT:
              self.head.setheading(RIGHT)