# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        visited = set()
        while True:
            visited.add(cur)
            if cur.val == p.val:
                break
                
            if cur.val < p.val:
                cur = cur.right
            else:
                cur = cur.left
        
        best = root
        curq = root
        while True:
            if curq in visited:
                best = curq
            if curq.val == q.val:
                break

            if curq.val < q.val:
                curq = curq.right
            else:
                curq = curq.left

        return best

        