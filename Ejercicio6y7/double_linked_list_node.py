from typing import Any, Union

class DoubleLinkedListNode:
    
    __slots__ = "element", "prev", "next"
    
    def __init__(self, element : Any, next = None, prev = None) -> None:
        self.element = element
        self.prev : Union[DoubleLinkedListNode, None] = prev
        self.next : Union[DoubleLinkedListNode, None] = next