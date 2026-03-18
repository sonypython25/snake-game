from turtle import Turtle

class Scoreb(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score=0
        with open("./data.txt","r") as file:
            self.high_score=int(file.read())
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"score:{self.score} highscore:{self.high_score}" ,align="center",font=("arial",28,"normal"))
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("./data.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update()
        

    # def game_over(self):
    #      self.goto(0,0)
    #      self.write(f"game over" ,align="center",font=("arial",28,"normal"))
       
    def increase(self):
        self.score+=1
        self.update()
        

        
        

    