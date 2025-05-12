from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Solution

# 1. Initialize two pointers left and right pointing to the head node
# 2. Move the right pointer n steps forward. Now the left and right pointers are separated by exactly n nodes
# 3. Move both the left and right pointers forward by 1 until right pointer reaches the last node. At this point, the left node is just before the n-th node from end
# 4. Relink the left node to the node at left's next to the next node.
# 5. Return head

# Time complexity
# In the worst case, we may have to traverse the entire list, therefore the time complexity is O(n).

# Space complexity
# We need constant or O(1) space to store the two pointers


def remove_nth_last_node(head: LinkedListNode, n: int):
    left, right = head, head

    for i in range(n):
        right = right.next

    if right is None:
        head = head.next
    else:
        while right.next is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
    return head


if __name__ == "__main__":
    ll = LinkedList()
    ll.create_linked_list([23, 28, 10, 5, 67, 39, 70, 28])
    n = 2
    remove_nth_last_node(ll.head, n)
    print(ll)
