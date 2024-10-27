from typing import Optional

from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_between(head: Optional[LinkedListNode], left: int, right: int):

    # Replace this placeholder return statement with your code
    dummy = LinkedListNode(0)
    dummy.next = head
    left_prev_ptr, left_ptr, right_ptr, right_next_ptr = dummy, head, head, head.next

    for _ in range(left - 1):
        if left_prev_ptr is not None and left_ptr is not None:
            left_prev_ptr = left_prev_ptr.next
            left_ptr = left_ptr.next

    for _ in range(right - 1):
        if right_ptr is not None and right_next_ptr is not None:
            right_ptr = right_ptr.next
            right_next_ptr = right_next_ptr.next

    right_ptr.next = None
    reverse_linked_list(left_ptr)
    left_prev_ptr.next = right_ptr
    left_ptr.next = right_next_ptr

    if left == 1:
        head = right_ptr

    return head


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.create_linked_list([4, 2, 7, 8, 9, 0, 2])
    head = reverse_between(ll1.head, left=3, right=7)
    ll1.head = head
    print(ll1)
