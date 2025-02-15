from typing import Optional

from linked_list_node import LinkedListNode


# Template for the linked list
class LinkedList:

    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head: Optional[LinkedListNode] = None

    # insert_node_at_head method will insert a LinkedListNode at
    # head of a linked list.
    def insert_node_at_head(self, node: LinkedListNode):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst: list):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def print_list(head: Optional[LinkedListNode], prefix: str):
    curr = head

    print(f"{prefix}: ", end="")
    while curr is not None:
        if curr.next is None:
            print(f"{curr.data}", end="")
        else:
            print(f"{curr.data} -> ", end="")
        curr = curr.next
    print()
