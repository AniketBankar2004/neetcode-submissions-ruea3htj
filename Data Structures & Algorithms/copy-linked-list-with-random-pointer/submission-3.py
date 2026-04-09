"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head ==None:
            return None
        curr = head 

        old_2_new = {}

        while curr:
            new_node = Node(curr.val)
            old_2_new[curr] = new_node
            curr = curr.next
        
        curr = head

        while curr:
            new_curr = old_2_new[curr]
            new_curr.next = old_2_new.get(curr.next)
            new_curr.random = old_2_new.get(curr.random)
            curr = curr.next
        
        return old_2_new[head]



        



        
            

            
        

        