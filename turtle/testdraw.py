import turtle

radius = 100
turtle.speed(0)
wn = turtle.Screen() 
for rings in range(10):
	turtle.penup()
	turtle.goto(0, -radius)
	turtle.pendown()
	turtle.circle(radius)
	radius += 10
turtle.color('red')
turtle.shape("turtle")
turtle.left(100)
turtle.forward(120)
turtle.getscreen()._root.mainloop()