from typing import Optional

from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Problem
# Given the head of a singly linked list, reverse the linked list and return its updated head.

# Constraints
# Let n be the number of nodes in a linked list.
# 1 <= n <= 500
# -5000 <= node.value <= 5000

# Solution
# - The algorithm reverses the linked list by traversing the list from the head to the tail while systematically reversing the direction of pointers between successive nodes.
# - For each node, we point its next pointer to its previous node, effectively reversing the direction of the sublist up to that point. Before altering the next pointer of any node, we store its next node in a temporary pointer to avoid losing track of subsequent nodes.
# - Finally, the head pointer is reassigned to the last node, marking the new head of the reversed list after the list has been fully reversed.

# Time complexity: O(n)
# Space complexity: O(1)


def reverse(head: Optional[LinkedListNode]):
    prev_node, curr_node, next_node = None, head, None

    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node
    return head


def print_linked_list(head: LinkedListNode):
    curr = head
    while curr != None:
        print(curr.data + " -> ")


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.create_linked_list([1, -2, 3, 4, -5, 4, 3, -2, 1])
    new_head = reverse(ll1.head)
    ll1.head = new_head
    print(ll1)
