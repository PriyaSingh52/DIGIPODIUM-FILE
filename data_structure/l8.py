colors = ['red','green','blue','orange','purple','brown','black','white','gray']

colors_with_a = []
colors_ending_with_n = []

for color in colors:
    if 'a' in color:
        colors_with_a.append(color)
    if color.endswith('n'): 
        colors_ending_with_n.append(color)

print(colors_with_a) 
print(colors_ending_with_n)       
