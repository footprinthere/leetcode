from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """time 81 / space 42"""

        def _preorder(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""

            output = f"{node.val}"
            left = _preorder(node.left)
            right = _preorder(node.right)

            if right == "":
                if left == "":
                    return output
                else:
                    return output + f"({left})"
            else:
                return output + f"({left})({right})"

        return _preorder(root)
