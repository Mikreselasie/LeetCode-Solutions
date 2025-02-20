# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode = head

        for i in range(n):
            currNode = currNode.next


        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while currNode:
            prev = prev.next
            currNode = currNode.next
        prev.next = prev.next.next

        return dummy.next