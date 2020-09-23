
a = [2, 3, 4, 5, 6, 7, 8]
b = [1, 3, 7, 8, 5, 9, 10, 11]
c = []

print("Lista a:")
print(a)
print("Lista b:")
print(b)
print("Elementos em comum entre elas: ")

set(a) & set(b)

print(set(a)&set(b)) #uma maneira mais simples

"""
for elemento in a:
  if elemento in b:
    if elemento not in c:
        c.append(elemento)
        print(c)
"""

