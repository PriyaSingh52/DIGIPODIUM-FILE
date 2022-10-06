from xml.dom.minidom import Element


elements = ["Hydrogen","Helium","Lithium"]
print(elements)
print('Individual elements:')
print(elements[0])
print(elements[1])
print(elements[2])



# changing a list element (mutability)
elements[1] = "Carbon"
print(elements)

print(elements, elements,elements,sep="\n")



# List of Numbers
list2 = [1,2,3,4,5,25,100]
print(list2)

# Mixed data list
list3 = ['Ravi',90,102,29,"B",False,5.786]
print(list3)


# Nested List
list4 = [[1,2,3],[3,4,5,7],[2,1]]
print(list4)