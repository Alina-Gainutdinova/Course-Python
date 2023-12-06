a = (4, 5, 8)
b = (4, 5, 8)
a = b
b[3] = 6
print(id(a))
print(id(b))

name1 = 'Alina'
name2 = 'Alina'

print(name1 == name2)
