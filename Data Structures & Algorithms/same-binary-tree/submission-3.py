# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and q:
            return False

        if not q and p:
            return False


        def dep(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            return max(dep(node.left), dep(node.right)) + 1

        def mapTree(node: Optional[TreeNode], l: List, i: int):
            if not node:
                return

            l[i] = node.val

            mapTree(node.left, l, 2*i+1)
            mapTree(node.right, l, 2*i+2)



        dp = dep(p) + 1
        dq = dep(p) + 1
        lp = [0] * 2**dp
        lq = [0] * 2**dq

        mapTree(p, lp, 0)
        mapTree(q, lq, 0)

        return lp == lq

        