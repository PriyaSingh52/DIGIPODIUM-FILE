x = [1,1,2,2,3,3,5,5,1,1,2,3,3,4,5,]
print(x, 'dupllicated values')
x = list(set(x))
print(x, 'cleaned list')

# data-structure conversion

x = [1,2,3,4,5]
print(x, 'list')

x = tuple(x)   # convert list to tuple
print(x, 'tuple')

x = set(x)      # convert tuple to set
print(x, 'set')


x = list(x)      # convert set to list
print(x, 'list')