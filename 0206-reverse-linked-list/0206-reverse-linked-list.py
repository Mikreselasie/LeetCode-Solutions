# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []

        currNode = head

        while currNode:
            temp.append(currNode.val)
            currNode = currNode.next
        if not len(temp):
            return
        temp.reverse()
        
        head = ListNode(temp[0])

        currNode = head

        for i in range(len(temp)):
            if i < len(temp)-1:
                currNode.next = ListNode(temp[i+1])
            else:
                currNode.next = None
            currNode = currNode.next
        return head