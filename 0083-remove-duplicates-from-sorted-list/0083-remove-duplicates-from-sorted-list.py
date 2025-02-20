# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()

        if not head:
            return
        curr = head

        my_set.add(curr.val)

        while curr and curr.next:
            my_set.add(curr.val)
            while curr.next and curr.next.val in my_set:
                curr.next = curr.next.next
            curr = curr.next
        return head 