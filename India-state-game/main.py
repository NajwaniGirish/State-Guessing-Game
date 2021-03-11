import turtle
import pandas as pd

screen = turtle.Screen()
screen.screensize(canvwidth=800, canvheight=800)
screen.setup(800, 800)
screen.title('India State Game')
image = "state_map.gif"

turtle.addshape(image)
turtle.shape(image)

df = pd.read_csv('28_states.csv')
state_list = df.state.to_list()
learn_state = []
guessed_list = []
while len(guessed_list) <= 28:
    answer = screen.textinput(title=f"{len(guessed_list)}/ 28 Guess State", prompt="guess the state name").title()
    if answer == 'Exit':
        for state in state_list:
            if state not in guessed_list:
                learn_state.append(state)
        states_to_learn = pd.DataFrame(learn_state)
        states_to_learn.to_csv('states_to_learn.csv')
        break

    if answer in state_list:
        guessed_list.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_date = df[df.state == answer]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(answer)


screen.exitonclick()

































# # def get_mouse_click_cord(x, y):
# #     print(x,',',y)
#
# turtle.onscreenclick(get_mouse_click_cord)
# turtle.mainloop()















