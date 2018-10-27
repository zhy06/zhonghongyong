from turtle import *
edge=15
setup(500,500,0,0)
pencolor("blue")
penup()
for i in range(25):
    fd(edge)
    pendown()
    left(90)
    fd(edge)
    left(90)
    edge=edge+10
fd(edge)
left(90)
fd(edge)
left(90)
