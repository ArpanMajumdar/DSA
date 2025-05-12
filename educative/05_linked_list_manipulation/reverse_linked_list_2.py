from typing import Optional

from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Problem
# Given a singly linked list with n nodes and two positions, left and right, the objective is to reverse the nodes of the list from left to right. Return the modified list.
# Constraints
# 1 <= n <= 500
# -5000 <= node.data <= 5000
# 1 <= left <= right <= n


def reverse_linked_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_between(head: Optional[LinkedListNode], left: int, right: int):
    # Handle base case
    if head is None or left == right:
        return head

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


def reverse_between_sol2(head: Optional[LinkedListNode], left: int, right: int):
    # Handle base case
    if head is None or left == right:
        return head

    # Create dummy node
    dummy = LinkedListNode(0)
    dummy.next = head

    prev = dummy
    for _ in range(left - 1):
        if prev is not None:
            prev = prev.next

    curr = prev.next
    print(f"prev = {prev.data}, curr = {curr.data}")

    for _ in range(right - left):
        next = curr.next
        curr.next = next.next
        next.next = prev.next
        prev.next = next
        print(f"prev = {prev.data}, curr = {curr.data}, next = {next.data}")

    return dummy.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.create_linked_list([3, 6, 7, 4, 2])
    head = reverse_between_sol2(ll1.head, left=2, right=4)
    ll1.head = head
    print(ll1)
