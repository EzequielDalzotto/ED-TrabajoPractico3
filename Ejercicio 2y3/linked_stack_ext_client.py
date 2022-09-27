from linked_stack_ext import LinkedStackExt
# from linked_stack import LinkedStack

pila = LinkedStackExt()

pila.push(12)
pila.push(14)
pila.push(17)
pila.push(40)
print(pila)

# for i in pila.multi_pop(2):
#     print(i)

# pila.replace_all(17,4)
# print(pila)
# print(pila._size)

pila.exchange()

print(pila)
print(pila._size)