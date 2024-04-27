from typing import Optional


class TreeNode:
    def __init__(
        self, val: int, left_val: Optional[int] = None, right_val: Optional[int] = None
    ) -> None:
        self.value = val
        self.left = TreeNode(left_val) if left_val is not None else None
        self.right = TreeNode(right_val) if right_val is not None else None

    def is_leaf(self):
        return self.left is None and self.right is None


def calculate_branch_sum(root: TreeNode) -> list[int]:
    branch_sums = []
    branch_sum_helper(root, running_sum=0, branch_sums=branch_sums)
    return branch_sums


def branch_sum_helper(tree_node: TreeNode, running_sum: int, branch_sums: list[int]):
    if tree_node is None:
        return

    running_sum += tree_node.value

    if tree_node.is_leaf():
        branch_sums.append(running_sum)
        return

    if tree_node.left is not None:
        branch_sum_helper(tree_node.left, running_sum, branch_sums)

    if tree_node.right is not None:
        branch_sum_helper(tree_node.right, running_sum, branch_sums)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4, left_val=8, right_val=9)
    root.left.right = TreeNode(5, left_val=10)
    root.right = TreeNode(3, left_val=6, right_val=7)

    branch_sums = calculate_branch_sum(root)
    print(f"Branch sums: {branch_sums}")


if __name__ == "__main__":
    main()
