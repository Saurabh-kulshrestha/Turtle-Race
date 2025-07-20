from turtle import Turtle, Screen
import random

is_race_on = False    # Initially, the race is off

screen = Screen()    # Creating a screen object
screen.setup(width=500, height=400)    # Setting the screen size to 500x400 pixels

# Asking the user to place a bet by entering a turtle color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of turtle colors
colors = ["red", "yellow", "green", "purple", "pink", "blue"]
position = 150
list_turtles = []    # List to store all the turtle objects

# Creating turtles with different colors and placing them at the starting line
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-230, position)
    position -= 50
    list_turtles.append(new_turtle)

# If the user has placed a bet, start the race
if user_bet:
    is_race_on =True

# Run the race while it's on
while is_race_on:
     for turtle in list_turtles:
         if turtle.xcor() > 230:    # If a turtle crosses the finish line (x > 230)
             is_race_on = False
             winning_color = turtle.pencolor()

             # Check if the user's bet matches the winning turtle
             if winning_color == user_bet:
                 print(f"You've won! The {winning_color} turtle is the winner!")
             else:
                 print(f"You've lost! The {winning_color} turtle is the winner!")
        # Move the turtle forward by a random distance between 0 and 10
         turtle.forward(random.randint(0, 10))


# Keeps the screen open until the user clicks on it
screen.exitonclick()
