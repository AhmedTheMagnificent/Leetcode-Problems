"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child == None:
                curr = curr.next
                continue
            nodeptr = curr.next
            curr.next = curr.child
            curr.child = None
            curr.next.prev = curr
            node = curr.next
            while node.next:
                node = node.next
            if nodeptr:
                node.next = nodeptr
                nodeptr.prev = node

            curr = curr.next
        return head