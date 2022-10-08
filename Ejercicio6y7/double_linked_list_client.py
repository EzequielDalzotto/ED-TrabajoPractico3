from double_linked_list import DoubleLinkedList
from util import h2

lista = DoubleLinkedList()

lista.append(10)
lista.append(11)
lista.append(12)
lista.append(15)

print(lista)

print(lista.__getitem__(2))

lista.__setitem__(2,100) #Funciona
print(lista)

lista.__delitem__(2) #Funciona
print(lista)

iterable = lista.__iter__() #Funciona
for i in iterable:
    print(i)

# print(lista.__getitem__(10)) #Lanza la exepcion esperada
