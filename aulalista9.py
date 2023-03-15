listad = [1,2,3,3,4,5,5,6]
listas = []
print(listad)
while listad:
    elemento = listad.pop(0)
    if elemento not in listas:
        listas.append(elemento)
        

print(listas)
        