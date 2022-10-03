from double_linked_list_abstract import DoubleLinkedListAbstract
from double_linked_list_node import DoubleLinkedListNode
from typing import Any, Iterator

class DoubleLinkedList(DoubleLinkedListAbstract):
    def __init__(self) -> None:
        self._header = DoubleLinkedListNode(None, None, None)
        self._size : int = 0

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, key: int) -> Any:
        if key < 0 and key >= self._size:
            raise Exception("El indice esta fuera de rango")

        i = 0
        actual = self._header.next # Inicio en el primer nodo.

        while actual: # Si existe
            if i == key: # Si el valor de i coincide con el de key
                return actual.element #Devuelvo el valor del nodo en el que estoy ubicado.
            actual = actual.next # Caso contrario continúo con el siguiente nodo.
            i += 1

    def __setitem__(self, key: int, value: Any) -> None:
        if key < 0 and key >= self._size:
            raise Exception("El indice esta fuera de rango")

        i = 0 
        actual = self._header.next # Inicio en el primer nodo
        
        while actual: # Si el nodo existe...
            if i == key: # Verifico si el índice coincide con el pasado por parámetro
                actual.element = value
            actual = actual.next
            i += 1

        
    def __delitem__(self, key: int) -> None:
        if key < 0 or key >= self._size:
            raise Exception("EL indice esta fuera de rango")

        i = 0

        actual = self._header.next # Arranco en el primer nodo de la lista.
        while actual: # Si existe...
            if i == key: # Si el i es igual a key => corto.
                break
            actual = actual.next # Continúo con el siguiente nodo.
            i += 1

        # Si previo existe => elimino el nodo actual haciendo que el siguiente del previo sea igual al siguiente de actual
        if actual.prev: 
            actual.prev.next = actual.next
        else:
            # Si previo no existe => se está queriendo eliminar el primer nodo.
            self._header.next = actual.next

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        actual = self._header.next
        
        #Si existe un nodo
        while actual:
            #Devuelve el elemento del nodo actual
            yield actual.element
            
            #Continúa con el siguiente.
            actual = actual.next

    def __str__(self) -> str:
        #Si la estructura está vacía => retorno siempre lo mismo.
        if self.is_empty():
            return "DoubleLinkedList()"
        
        res = "" # inicializo resultado con el string vacío

        actual = self._header.next # Inicio con el primer nodo de la estructura.

        while actual: # Si el elemento actual no es None
            # Lo proceso
            res += str(actual.element) + ", "
            # Continúo con el siguiente.
            actual = actual.next

        # Quito las dos últimas posiciones del string.
        res = res[:-2]

        return f"LinkedList({res})"

    def is_empty(self) -> bool:
        return self._size == 0

    def append(self, elem: Any) -> None:
        nuevo_nodo = DoubleLinkedListNode(elem)
        # Si la lista está vacía => el nuevo nodo es el primero.
        if self.is_empty():
            self._header.next = nuevo_nodo
        else:
            # Caso contrario => me muevo hasta el final...
            actual = self._header

            while actual.next:
                actual = actual.next

            #Asigno como previo del nuevo nodo al actual
            nuevo_nodo.prev= actual
            # Agrego el nuevo nodo como siguiente del último.
            actual.next = nuevo_nodo

        self._size += 1