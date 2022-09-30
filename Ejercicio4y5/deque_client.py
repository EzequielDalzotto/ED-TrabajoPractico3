from deque import Deque
from util import h2
deque = Deque()

deque.add_last(12)
deque.add_first(13)
deque.add_first(17)
deque.add_last(18)
deque.add_last(19)
deque.add_last(20)

h2("Print:")
print(deque)

# h2("is_empty:")
# print(deque.is_empty())

# h2("__len__")
# print(deque.__len__())

# h2("First:")
# print(deque.first())

# h2("Last:")
# print(deque.last())

h2("Delete first")
deque.delete_first()
print(deque)

h2("Delete last")   #Unico metodo con problemas
deque.delete_last() #Posible solucion usar doble enlace en cada nodo
print(deque)

print(deque.__len__())
