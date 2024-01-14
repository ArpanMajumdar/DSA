from typing import Optional


class TreeNode:
    def __init__(
        self, val: int, left_val: Optional[int] = None, right_val: Optional[int] = None
    ) -> None:
        self.val = val
        self.left = TreeNode(left_val) if left_val is not None else None
        self.right = TreeNode(right_val) if right_val is not None else None

# Time complexity: O(log(n)) average case, O(n) worst case
# Space complexity: O(1) average case, O(n) worst case
def find_closest_val_in_bst(root: TreeNode, target: int):
    curr_node = root
    closest_val = float("inf")

    while curr_node is not None:
        if abs(target - curr_node.val) < abs(target - closest_val):
            closest_val = curr_node.val

        if target < curr_node.val:
            curr_node = curr_node.left
        elif target > curr_node.val:
            curr_node = curr_node.right
        else:
            break

    return closest_val


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2, left_val=1)
    root.right.left = TreeNode(13, right_val=14)
    root.right.right = TreeNode(22)

    target = 12
    closest_val = find_closest_val_in_bst(root, target)
    print(f"closest_value to {target} is {closest_val}.")


if __name__ == "__main__":
    main()
