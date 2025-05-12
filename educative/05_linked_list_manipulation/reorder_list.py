from typing import Optional

from linked_list import LinkedList, print_list
from linked_list_node import LinkedListNode

# Problem
# Given the head of a singly linked list, reorder the list as if it were folded on itself. For example, if the list is represented as follows:
# Input: L0 -> L1 -> L2 -> ... -> Ln-2 -> Ln-1 -> Ln
# Output: L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...
# You don’t need to modify the values in the list’s nodes; only the links between nodes need to be changed.
# Constraints
# - The range of number in the nodes in the list is [1, 500]
# - -5000 <= node.value <= 5000

# Solution
# 1. Use the fast and slow pointer approach to find the middle of the list. If there are two, middle nodes, choose the second node.
# 2. Reverse the second half of the linked list
# 3. Merge both halves of the linked lists alternatively.

# Time complexity: O(n)
# Space complexity: O(1)


def reorder_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    # Base case
    if head is None or head.next is None:
        return head

    slow_ptr, fast_ptr = head, head

    # Find mid-point of list
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Break list into two parts from mid-point
    mid_ptr = slow_ptr
    head2 = mid_ptr.next
    mid_ptr.next = None

    reversed_head = reverse_list(head2)
    merge_lists(head, reversed_head)
    return head


def reverse_list(head: Optional[LinkedListNode]):
    if head is None or head.next is None:
        return head

    prev_ptr, curr_ptr, next_ptr = None, head, None

    while curr_ptr is not None:
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr

    return prev_ptr


def merge_lists(head1: Optional[LinkedListNode], head2: Optional[LinkedListNode]):
    ptr1, ptr2 = head1, head2

    while ptr1 is not None and ptr2 is not None:
        temp = ptr1.next
        ptr1.next = ptr2
        ptr1 = temp

        temp = ptr2.next
        ptr2.next = ptr1
        ptr2 = temp

    return head1


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.create_linked_list([6, 6, 7, 7, 8, 8, 9, 9, 0, 0])
    head = reorder_list(ll1.head)
    ll1.head = head
    print(ll1)
