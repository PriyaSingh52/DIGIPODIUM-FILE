m = "This is an Example"
print(len(m))
for i, v in enumerate(m):
     print(f'{i} --> {v}')



# slicing
print(m[5:7]) # is
print(m[8:10]) # an

s = 'digipodium'
slice = s[0:4]
slice1 = s[:4]
slice2 = s[4:]
slice3 = s[4:len(s)]
print(slice)
print(slice1)
print(slice2)
print(slice3)



amt = '$3000'
print(amt) #error
print(int (amt[1:]))


rr = '1,143 ratings | 452 answered questions'