# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isBalancedBool = True
    def balancedNum(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        lbalNum = self.balancedNum(node.left)
        rbalNum = self.balancedNum(node.right)
        if abs(lbalNum - rbalNum) > 1:
            self.isBalancedBool = False
        return max(lbalNum, rbalNum) + 1


          

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balancedNum(root)

        return self.isBalancedBool