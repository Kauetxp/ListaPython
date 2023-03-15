#Varrendo a lista de varias formas diferentes

lista = ["Camila","Alexis","José","Kauê"]

#Utilizando FOR

for i in range(len(lista)):
    print("O elemento",i+1,"da lista é:",lista[i])
    
#utilizando for de outro jeito

numeros = [8,7,6,5,4]
for numero in numeros:
    print(numero," - com for")
    
#utilizando while (eu amo)

i = 0
while i < len(lista):
    print("O item",i+1,"é",lista[i]," - com while")
    i += 1
    