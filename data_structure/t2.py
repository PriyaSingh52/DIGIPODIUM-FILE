x = 1, 2, 3, 3, 54, 5
print(x)
print(type(x))

a, b = 10, 20 # 2 values are stored in 2 variables
print(a,b)
a = 10, 20  # 2 values are packed inn 1 variable as tuple
print(a,type(a))

# special case
x, x2, x3, *y = 1, 2, 3, 3, 54, 5    # 1 value is stored in x and rest in y as a list
print(x, x2,x3,y)
print(type(x), type(y))