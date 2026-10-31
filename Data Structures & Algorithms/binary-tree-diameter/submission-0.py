# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        best = 0

        def subTree(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return -1

            l = subTree(node.left) + 1
            r = subTree(node.right) + 1

            print(f"best: {best} val: {node.val} l: {l} r: {r}")
            if l + r > best:
                best = l + r
            return max(l, r)


        cur = subTree(root)

        if cur > best:
            return cur
        else:
            return best      