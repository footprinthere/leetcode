from typing import Optional


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Optional["Node"],
        topRight: Optional["Node"],
        bottomLeft: Optional["Node"],
        bottomRight: Optional["Node"],
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        """time 27 / space 22"""

        return bitwise_or(quadTree1, quadTree2)


def bitwise_or(node1: "Node", node2: "Node") -> "Node":
    # Either is 1 -> 1
    if is_leaf_of(node1, True) or is_leaf_of(node2, True):
        return Node(True, True, None, None, None, None)

    # Either is 0 -> the other side
    if is_leaf_of(node1, False):
        return node2
    if is_leaf_of(node2, False):
        return node1

    # Recursion
    rec_results = [
        bitwise_or(ch1, ch2)
        for ch1, ch2 in zip(get_children(node1), get_children(node2))
    ]
    if all(r.isLeaf and r.val == rec_results[0].val for r in rec_results):
        # All children are leaf and have the same value -> merger
        return Node(rec_results[0].val, True, None, None, None, None)
    else:
        return Node(False, False, *rec_results)


def is_leaf_of(node: "Node", val: bool) -> bool:
    return node.isLeaf and (node.val is val)


def get_children(node: "Node") -> list["Node"]:
    return [node.topLeft, node.topRight, node.bottomLeft, node.bottomRight]
