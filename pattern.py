import turtle
turtle.pensize(3)
turtle.bgcolor("black")
turtle.speed(0)
b=["red","blue","yellow","purple"]
for i in range(9):
    for a in b:
        turtle.color(a)
        turtle.forward(50)
        turtle.right(20)
        # turtle.position(0)
        
# for i in range(9):
#     for a in b:
#         turtle.color(a)
#         turtle.square(100)
#         turtle.left(20)
turtle.mainloop()        
