from typing import Optional

from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse(
    head: Optional[LinkedListNode], k: int
) -> tuple[Optional[LinkedListNode], Optional[LinkedListNode]]:
    prev_node, curr_node, next_node = None, head, None

    for i in range(k):
        if curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node, curr_node


def reverse_k_groups(
    head: Optional[LinkedListNode], k: int
) -> Optional[LinkedListNode]:
    # Create a dummy node and attach before head
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    while ptr is not None:
        tracker = ptr

        for i in range(k):
            if tracker is None:
                break

            tracker = tracker.next

        # This group doesn't has k nodes
        if tracker is None:
            break

        prev, current = reverse(ptr.next, k)
        last_node_of_rev_group = ptr.next
        if last_node_of_rev_group is not None:
            last_node_of_rev_group.next = current
        ptr.next = prev
        ptr = last_node_of_rev_group
    return dummy.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    new_head = reverse_k_groups(ll1.head, k=3)
    ll1.head = new_head
    print(ll1)
