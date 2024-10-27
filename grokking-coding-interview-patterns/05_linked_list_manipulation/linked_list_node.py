from typing import Any, Optional


class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data: Any, next=None):
        self.data = data
        self.next: Optional[LinkedListNode] = next
