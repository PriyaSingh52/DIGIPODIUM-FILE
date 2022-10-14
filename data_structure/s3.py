a = {'Ram','Shyam','Hari','Gita','Sita'}
b = {'Alex','Mark','Eliza','Benny','Sunny'}
c =  {'Ram','Alex','Gita','Tanya','Sergei'}

# Union
ab = a | b
print('union=>, ab')
#or
ab = a.union(b)
print("union=>", ab)

# intersection
ac = a & c  # a.intersection(c) also works
print('intersection=>', ac)

abi = a & b
print('intersection=>', abi)

# difference
ac = a -c
print('difference=>', ac)

ca = c - a
print('difference=>', ca)

# symmetric difference
ac = a^c # a.symmetric_difference(c) also works
print('symmetri_differencec=>',ac)
