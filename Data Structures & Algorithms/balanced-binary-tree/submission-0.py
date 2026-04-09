# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = [True]

        def maxHeight(root):
            if not root:
                return 0
            
            rightHeight = maxHeight(root.right)
            leftHeight = maxHeight(root.left)

            if(abs(leftHeight-rightHeight)>1):
                isBalanced[0] = False
            
            return max(maxHeight(root.left),maxHeight(root.right))+1
    
        maxHeight(root)
        return isBalanced[0]
        
        
        