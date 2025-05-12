from tree_node import TreeNode

# Problem

# Invert binary tree by swapping each node's left and right subtrees, thus creating a mirror image of the tree.

# Solution

# - Perform post order traversal on the left subtree
# - Perform post order traversal on the right subtree
# - Swap the left and right children of the root node


def mirror_binary_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return root

    if root.left is not None:
        mirror_binary_tree(root.left)
    if root.right is not None:
        mirror_binary_tree(root.right)

    # Swap left and right subtrees
    temp = root.left
    root.left = root.right
    root.right = temp

    return root
