# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0

        multiplier = 1

        while l1:
            sum1 += l1.val * multiplier
            l1 = l1.next
            multiplier = multiplier * 10

        multiplier = 1

        while l2:
            sum2 += l2.val * multiplier
            l2 = l2.next
            multiplier = multiplier * 10
        
        sum3 = sum1 + sum2

        sum3 = str(sum3)
        n = len(sum3)
        l3 = ListNode(val = int(sum3[n-1]))
        curr = l3

        for i in range(n-1-1,-1,-1):
            curr.next = ListNode(val=int(sum3[i]))
            curr = curr.next
        
        return l3




