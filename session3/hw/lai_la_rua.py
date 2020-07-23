from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

penup()
goto(-100,100)
pendown()

color_count = 0
for edge in range(3, 8):
  color(colors[color_count])
  for i in range(edge):
    forward(50)
    left(360/edge)
  color_count += 1 # equal to color_count = color_count + 1

penup()
goto(50,100)
pendown()

for i in range(5):
    for c in colors:
        color(c)
        fillcolor(c)
        begin_fill()
        for i in range(2):
            forward(50)
            left(90)
            forward(100)
            left(90)
        end_fill()
        forward(50)




mainloop()
