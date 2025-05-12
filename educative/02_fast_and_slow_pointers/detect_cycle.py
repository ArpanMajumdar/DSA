from linked_list import LinkedList
from linked_list_node import LinkedListNode


def detect_cycle(head: LinkedListNode) -> bool:
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next  # type: ignore
        fast_ptr = fast_ptr.next.next

        if fast_ptr == slow_ptr:
            return True

    return False
