import turtle
import pandas


def right(player_input, x_axis, y_axis):
    turtel1 = turtle.Turtle()
    turtel1.speed(0)
    turtel1.penup()
    turtel1.hideturtle()
    turtel1.goto(x_axis, y_axis)
    turtel1.write(player_input, align='center', font=('Arial', 20, 'bold'))


df = pandas.read_csv('50_states.csv')
states = df.state.to_list()
screen = turtle.Screen()
screen.addshape('blank_states_img.gif')
turtel = turtle.Turtle()
turtel.shape('blank_states_img.gif')
title = 'guess the state'
for a in range(len(states)):
    player_input = screen.textinput(title=title, prompt='write the state name')
    if player_input in states:
        title = 'right guess'
        state_data = df[df['state'] == player_input]

        x_axis = state_data.x
        y_axis = state_data.y

        right(player_input, x_axis, y_axis)
        print('correct')
screen.exitonclick()
