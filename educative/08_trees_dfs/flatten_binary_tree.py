from tree_node import TreeNode

# Problem

# Given the root of a binary tree, the task is to flatten the tree into a linked list using the same TreeNode class.
# The left child pointer of each node in the linked list should always be NULL, and the right child pointer should point
# to the next node in the linked list. The nodes in the linked list should be in the same order as that of the preorder
# traversal of the given binary tree.

# Solution

# Traverse the binary tree, and for each node, check if it has a left child.
# If the left child exists, find the rightmost node in the left subtree.
# Point the right pointer of the rightmost node to the right child of the current node.
# Set the current node’s right pointer to the current node’s left pointer.
# Set the current node’s left child to NULL.
# Repeat the steps above until the entire binary tree has been traversed.


def flatten_tree(root: TreeNode) -> TreeNode:
    # Base case
    if root is None:
        return root

    current = root

    while current is not None:
        if current.left is not None:
            # Find the rightmost node of left subtree
            rightmost_node = find_rightmost_node(current.left)
            rightmost_node.right = current.right
            current.right = current.left
            current.left = None

        current = current.right
    return root


def find_rightmost_node(root: TreeNode) -> TreeNode:
    if root is None:
        return root

    current = root
    while current.right is not None:
        current = current.right
    return current


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    curr_node = root
    flatten_tree(root)

    while curr_node is not None:
        print(curr_node.data, end=" -> ")
        curr_node = curr_node.right
