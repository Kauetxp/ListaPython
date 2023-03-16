import time

ej = []
print("Membros da banda: ")
ej.append("Mostarda")
ej.append("Asaph")
ej.append("Lacaze")
ej.append("Kaue")
print(ej)

time.sleep(2)

print("Foram adicionados mais membros: ")
ej.append("Moura")
ej.append("Davi")

print(ej)

time.sleep(2)

n = input("Adicione um novo membro: ")

ej.append(n)
print(ej)
time.sleep(2)

print("Dois membros foram removidos da banda")
del ej[-2]
del ej[2]

print("Agora a banda está assim: \n",ej)