# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(node):
            if node is None:
                return 0
            else:
                return 1 + max(getHeight(node.left), getHeight(node.right))

        def checkBalance(root):
            if root is None:
                return True
            else:
                balance = getHeight(root.right) - getHeight(root.left)
                if balance > 1 or balance < -1:
                    return False
                else:
                    return checkBalance(root.left) and checkBalance(root.right)
                

        return checkBalance(root)




      

       

        
        