from turtle import *
speed ('fastest')
i = 1
while True:
    fd(10 + i)

    for j in range (6):
       fd(100)
       lt(360/6)
       print(i,j)

    left(360/6)
    i  += 5
    write(i)
    if i > 500:
        break

mainloop()    

