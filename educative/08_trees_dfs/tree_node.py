from typing import Optional


class TreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
