from typing import Tuple

from tree_node import TreeNode

# Problem

# Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree is the 
# length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Solution
# - Start with the assumption that the diameter is 0.
# - Calculate the diameter of the left sub-tree and right sub-tree of the root node using the following recursive process:
#   - At a leaf node, the diameter and height with respect to its children is 0 and 1, respectively.
#   - For a non-leaf node, calculate the heights as well as the diameters of the left and right sub-trees. If the diameter 
#     passes through this node, then the diameter is the sum of the heights of the two sub-trees. 
#     Otherwise, it is the greater of the diameters of the two sub-trees.
# - Update the diameter as the greater of two values:
#   - the sum of the heights of the left and right sub-trees,
#   - the greater of the diameters of the two sub-trees.


def diameter_of_binaryTree(root: TreeNode) -> int:
    if root is None:
        return 0

    _, diameter = calculate_tree_height_diameter(root, 0)
    return diameter


def calculate_tree_height_diameter(root: TreeNode, diameter: int) -> Tuple[int, int]:
    if root is None:
        return 0
    left_tree_height, _ = (
        calculate_tree_height_diameter(root.left, diameter) if root.left else (0, 0)
    )
    right_tree_height, _ = (
        calculate_tree_height_diameter(root.right, diameter) if root.right else (0, 0)
    )
    height = 1 + max(left_tree_height, right_tree_height)
    diameter = max(diameter, left_tree_height + right_tree_height)
    return height, diameter


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    diameter = diameter_of_binaryTree(root)
    print(f"{diameter=}")
