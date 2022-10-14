x = [2,2,2,2,2,2,3,3,3,3,1,1,1,1]

print(x.count(3))
print(x.count(2))
print(x.count(22))

print(x.index(3))
print(x.index(2))
#print(x.count(22))   #valueError

z = x    # not a good idea, it's a reference
y = x.copy()
z.append(10)
z.append(20)
print(x is z)
print(x is y)
print(x)
print(y)
print(z)