from turtle import Turtle, Screen
import pandas

data=pandas.read_csv("50_states.csv")
states_list=data["state"].tolist()
# print(states_list)


tim=Turtle()
tim.penup()
tim.hideturtle()
screen=Screen()
screen.bgpic("blank_states_img.gif")
selected_state_list=[]
while(len(selected_state_list)<=50):
    if len(selected_state_list)==50:
        tim.goto(0,0)
        tim.write("YOU WIN!",False,"center",("courier",24,"normal"))
        break
    state=screen.textinput(f"{len(selected_state_list)}/50 States Correct","What's another state name?")
    state=state.title()
    if(state=="Exit"):
        break
    if state in states_list:
        selected_state_list.append(state)
        selected_state=data[data["state"]==state]
        tim.goto(int(selected_state['x']),int(selected_state['y']))
        series=selected_state['state']
        tim.write(selected_state['state'].item())

state_dict={}

state_dict["state"]=[i for i in states_list if not i in selected_state_list]

df=pandas.DataFrame(state_dict)
df.to_csv("states_to_learn.csv")

screen.exitonclick()