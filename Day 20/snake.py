from turtle import Turtle
Starting_Position = [(0,0),(-20,0),(-40,0)]
distance = 20

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()


    def create_snake(self):
        for i in Starting_Position():
            object = Turtle("square")
            object.color("white")
            object.penup()
            object.goto(i)
            self.segement.append(object)

    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            x= self.segment[i - 1].xcor()
            y=self.segment[i - 1].ycor()
            self.segment[i].goto(x,y)
        self.segment[0].forward(distance)
    pass