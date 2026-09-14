# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head

        if head.next != None:
            prev = head
            curr = head.next
            h = curr
            prev.next = None
        else:
            return head

        while curr.next != None:
            h = curr.next
            curr.next = prev
            prev = curr
            curr = h
        
        curr.next = prev
        
        return h

        

        