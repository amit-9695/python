import turtle
t=turtle.Turtle()
t.speed(100)
turtle.bgcolor('black')
for i in range (320):
    t.color('cyan')
    t.circle(i)
    t.left(4)
turtle.done()