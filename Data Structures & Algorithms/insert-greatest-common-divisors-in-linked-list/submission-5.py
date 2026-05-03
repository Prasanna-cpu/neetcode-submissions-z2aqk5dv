# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gcd(self, a, b):
        while b:
            a , b = b , a % b
        return a


    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            a = curr.val
            b = curr.next.val

            g = self.gcd(a, b)

            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        return head