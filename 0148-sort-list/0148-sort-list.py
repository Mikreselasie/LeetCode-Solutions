# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp_head = head
        while temp_head:
            arr.append(temp_head.val)
            temp_head = temp_head.next
        
        arr.sort()
        temp_head = head
        for i in range(len(arr)):
            temp_head.val = arr[i]
            temp_head = temp_head.next

        return head