from linked_stack_ext_abstract import LinkedStackExtAbstract
from linked_stack import LinkedStack
from list_node import ListNode
from typing import Any, List

class LinkedStackExt(LinkedStack,LinkedStackExtAbstract):
    def multi_pop(self, num: int) -> List[Any]:

        if self.is_empty():
            raise Exception("La estructura esta vacia")
        
        resultado = []

        while num != 0:
            resultado.append(self.pop())
            num-=1
        return resultado

    def replace_all(self, param1: Any, param2: Any) -> None:

        #Se crea una pila temporal
        temp_stack = LinkedStack()

        #Se pushea todos los elementos de la pila a la temporal y se reemplaza ocurrencias
        while self._head != None:
            if self._head.element == param1:
                self._head.element = param2
            temp_stack.push(self._head.element)
            self._head=self._head.next

        #Pushea la pila temporal a la principal sin modificar su tamaño
        for i in range (0,self._size):
            nuevo_tope = ListNode(temp_stack.pop(), self._head)
            self._head = nuevo_tope

    def exchange(self) -> None:
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        tope_viejo = self.pop()#guarda y quita el anterior tope
        temp_stack= LinkedStack()#Crea una pila temporal

        #Recorre la pila y pushea hasta el anteultimo elemento a la temporal
        while self._head.next != None:
            temp_stack.push(self._head.element)
            self._head=self._head.next
        
        inicio_viejo=self.pop()#Guarda y quita el ultimo elemento

        self.push(tope_viejo)#Pushea primero el anterior tope
        #Pushea todos los elementos para dejarlos igual
        for i in range(0,self._size-1):
            nuevo_tope = ListNode(temp_stack.pop(), self._head)
            self._head = nuevo_tope
        #Pushea como ultimo elemento el anterior inicio
        self.push(inicio_viejo)

