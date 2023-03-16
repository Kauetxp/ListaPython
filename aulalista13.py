lista = [255,4,8,1]
trocado = True
while trocado:
    trocado = False
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            trocado = True
            lista[i],lista[i+1] = lista[i+1],lista[i]

print(lista)
