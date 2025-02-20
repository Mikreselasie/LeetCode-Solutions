# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0

        curr = head
        while curr:
            curr = curr.next
            count += 1
            if count > 10000:
                return True
        return False
        