from typing import Any
from deque_abstract import DequeAbstract
from linked_queue import LinkedQueue
from list_node import ListNode

class Deque(LinkedQueue,DequeAbstract):
    def __len__(self) -> int:
        return super().__len__()

    def __str__(self) -> str:
        return super().__str__()

    def is_empty(self) -> bool:
        return super().is_empty()
    
    def first(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        return self._front.element
    
    def last(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        return self._back.element

    def add_first(self, element: Any) -> None:
        
        nuevo_nodo = ListNode(element,None)

        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            nuevo_nodo.next=self._front
            self._front = nuevo_nodo
        self._size+=1

    def add_last(self, element: Any) -> None:
        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        #Elimina el elemento al principio de la cola
        self._front = self._front.next
        self._size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("La estructura esta vacia")

        previo= None
        actual= self._front.next
        i=0

        while actual: # Si existe...
            if i == self._size - 2: # Si el i es igual a key => corto.
                break
            previo = actual # Guardo el valor de actual en previo.
            actual = actual.next # Continúo con el siguiente nodo.
            i += 1
            
        if previo: 
            previo.next = actual.next
        else:
            # Si previo no existe => se está queriendo eliminar el primer nodo.
            self._front.next = actual.next
