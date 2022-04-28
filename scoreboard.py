from turtle import Turtle

ALIGN = "center"
FONT = ("Arial",24, "normal")


class Scoreboard (Turtle):

    def __init__(self):#crear constructor
        super().__init__()
        self.score = 0 #atributo que guarda score y lo actualiza
        self.goto(0, 270)
        self.color('white')
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write (f'El puntaje es:{self.score}',font=FONT, align=ALIGN)#para representar un tablero de puntos. la F antes de las comillas indica que se va a recibir una variable en este caso self.score

    def increase_score(self): #metodo para sumar puntaje cad vez q ejecute
        self.clear()
        self.score += 1 #sumar automáticamente de uno en uno
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write ('juego terminado :(',font=FONT, align=ALIGN)