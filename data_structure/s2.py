# we can make a set from a list
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have dupicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# set cannot have mutable items
#my_set = {1, 2, [3,4]}        # [3,4] is a mutable list , this wil cause an error



# Modifying a set
my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([4, 5], {1, 6, 8})
print(my_set)

