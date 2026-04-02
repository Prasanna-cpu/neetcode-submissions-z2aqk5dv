# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt_node = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_node
        
        first = head
        second = prev

        while second:
            t1 , t2  = first.next , second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
            
        