from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """ time 73 / space 94 """
        
        sums = []               # sums[level + 1] = 각 level의 합
        stack = [(1, root)]     # (level, node)

        # DFS식 traverse
        while stack:
            level, node = stack.pop()

            if level <= len(sums):
                sums[level - 1] += node.val
            else:
                sums.append(node.val)

            if node.left is not None:
                stack.append((level + 1, node.left))
            if node.right is not None:
                stack.append((level + 1, node.right))

        if k > len(sums):
            return -1
        else:
            return sorted(sums, reverse=True)[k - 1]


if __name__ == "__main__":
    n4 = TreeNode(4)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n4, n6)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    n8 = TreeNode(8, n2, n1)
    n9 = TreeNode(9, n3, n7)
    n5 = TreeNode(5, n8, n9)

    answer = Solution().kthLargestLevelSum(n5, 2)
    print(answer)
