# Getting a list slice
l = [10,20,30,40,50,60,70,80,90,100]
slice1 = l[3:-2]
print(slice1)

# Append Function
fruits = []
fruits.append("apple")
fruits.append("Banana")
fruits.append("cherry")
fruits.append("Guava")
print(fruits)


y=l.append(["nikita","priya"])
print(y)

# Extend function-
fruits = ['Apple','Banana','Cherry', 'Guava']
dry_fruits = ['Almond','cashew', 'Pistachio','Walnut']
print(len(fruits))
fruits.append(dry_fruits)
print(fruits)

# sort function-
fruits = ['Cherry','Guava','Apple', 'Banana']
fruits.sort()
print(fruits)

# Remove function-
fruits = ['Cherry','Guava','Apple', 'Banana','Grapes']
fruits.remove('Cherry')
fruits.pop(3)
fruits.pop()
print(fruits)
