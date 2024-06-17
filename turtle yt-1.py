import turtle

akir = turtle.Turtle()

#learning forward and leftright method
#akir.forward(100)
#akir.left(45)
#akir.forward(100)
#akir.right(90)
#akir.forward(100)

#learning how to color the border
akir.color("blue", "cyan")#we can use #values for certain color and rgb values as well

#learning how to create a square
akir.begin_fill()#adding color inside the shape
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.end_fill()#adding color inside the shape


akir.penup()#seperating to shapes
akir.forward(150)
akir.pendown()#seperating to shapes

akir.begin_fill()
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.left(90)
akir.forward(100)
akir.end_fill()


turtle.done()