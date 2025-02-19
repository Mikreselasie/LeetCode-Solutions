# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        currNode = head

        while currNode:
            temp.append(currNode.val)
            currNode = currNode.next
        if not len(temp):
            return
        
        temp.reverse()
        head2 = ListNode(temp[0])

        currNode = head2

        for i in range(len(temp)):
            if i < len(temp)-1:
                currNode.next = ListNode(temp[i+1])
            else:
                currNode.next = None
            currNode = currNode.next
        
        nodes1 = head
        nodes2 = head2

        for i in range(len(temp)):
            if nodes1.val != nodes2.val:
                return False
            nodes1 = nodes1.next
            nodes2 = nodes2.next
        return True
            