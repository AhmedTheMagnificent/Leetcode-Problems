# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        curr = self.removeNodes(head.next)
        if curr.val > head.val:
            return curr
        else:
            head.next = curr
            return head