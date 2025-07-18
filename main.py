from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "green", "purple", "pink", "blue"]
position = 150
list_turtles = []

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-230, position)
    position -= 50
    list_turtles.append(new_turtle)

if user_bet:
    is_race_on =True
while is_race_on:
     for turtle in list_turtles:
         if turtle.xcor() > 230:
             is_race_on = False
             winning_color = turtle.pencolor()
             if winning_color == user_bet:
                 print(f"You've won! The {winning_color} turtle is the winner!")
             else:
                 print(f"You've lost! The {winning_color} turtle is the winner!")

         turtle.forward(random.randint(0, 10))



screen.exitonclick()