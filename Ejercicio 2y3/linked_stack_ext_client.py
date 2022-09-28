from util import h1, h2
from linked_stack_ext import LinkedStackExt

pila = LinkedStackExt()

pila.push(12)
pila.push(14)
pila.push(17)
pila.push(40)
pila.push(50)
pila.push(22)
pila.push(17)
pila.push(19)
pila.push(17)

h1("Impresion de la pila")
print(pila)

h2("Multi pop:")
for i in pila.multi_pop(2):
    print(i)

h2("replace_all:")
pila.replace_all(17,4)
print(pila)
print(pila._size)

h2("Exchange")
pila.exchange()

print(pila)
print(pila._size)