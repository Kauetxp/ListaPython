lista = []
trocado = True
num = int(input("Quantos elementos você deseja: "))
for i in range(num):
    val = float(input("Entre com um número: "))
    lista.append(val)
while trocado:
    trocado = False
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            trocado = True
            lista[i], lista[i+1] = lista[i+1],lista[i]
print("Lista ordenada:\n",lista)
