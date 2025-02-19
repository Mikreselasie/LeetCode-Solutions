# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.length = 0

        currNode = head

        while currNode:
            self.length += 1
            currNode = currNode.next
        
        self.position = self.length - n

        if self.position == 0:
            head = head.next
            return head

        currIdx = 1
        currNode = head
        
        while currIdx < self.position:

            currNode = currNode.next
            currIdx += 1
        

        currNode.next = currNode.next.next

        return head