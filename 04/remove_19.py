from typing import Optional


class ListNode:
    val: int
    next: "ListNode"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def scan(self) -> list[int]:
        result = [self.val]
        node = self

        while node.next is not None:
            node = node.next
            result.append(node.val)

        return result

    @classmethod
    def from_arr(cls, arr: list[int]) -> "ListNode":
        dummy_head = ListNode(-1)
        prev = dummy_head

        for val in arr:
            prev.next = ListNode(val)
            prev = prev.next

        return dummy_head.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        " time 61% / space 57% "
        
        # scan
        node = head
        node_list: list[ListNode] = []
        while node is not None:
            node_list.append(node)
            node = node.next

        # add dummy head
        dummy = ListNode(-1, head)
        node_list.insert(0, dummy)

        # remove
        target = node_list[-n]
        prev = node_list[-n - 1]

        prev.next = target.next
        del target

        return dummy.next


if __name__ == "__main__":
    head = ListNode.from_arr([1])
    n = 1

    print(head.scan())

    answer = Solution().removeNthFromEnd(head, n)
    print(answer.scan())
