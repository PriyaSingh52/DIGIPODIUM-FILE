from turtle import *
bgcolor('black')
speed ('fastest')

colors = ['red','green','blue','magenta','yellow','orange']
for i in range(360):
    pencolor(colors[i%6])
    width(i/100 + 1)
    fd(i)
    left(59)

mainloop()



   