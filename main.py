import turtle
import pandas


def right(name, xcord, ycord):

    turtel1 = turtle.Turtle()
    turtel1.speed(0)
    turtel1.penup()
    turtel1.hideturtle()
    turtel1.goto(xcord, ycord)
    turtel1.write(name, align='center', font=('Arial', 20, 'bold'))

total_states=50
states_left=0
df = pandas.read_csv('50_states.csv')
states = df.state.to_list()
screen = turtle.Screen()
screen.addshape('blank_states_img.gif')
turtel = turtle.Turtle()
turtel.shape('blank_states_img.gif')
title = 'guess the state 0/50'
for a in range(len(states)):
    player_input = screen.textinput(title=title, prompt='write the state name')
    print(player_input)
    if player_input.title() in states:
        states_left += 1
        title = f'right guess{states_left}/{total_states}'
        state_data = df[df.state == player_input.title()]

        x_axis = int(state_data.x)
        y_axis = int(state_data.y)
        right(player_input, x_axis, y_axis)


screen.exitonclick()
