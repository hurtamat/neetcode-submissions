"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}
        cloned[node] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            curNew = cloned[cur]

            for nei in cur.neighbors:
                if nei not in cloned:
                    newNode = Node(nei.val)
                    cloned[nei] = newNode
                    q.append(nei)
                
                curNew.neighbors.append(cloned[nei])

        return cloned[node]



            

        