class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        dic = set()
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


        def dfs( i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0" or (i, j) in dic:
                return

            dic.add((i, j))

            for d in dirs:
                curI, curJ = d
                if not (i + curI, j + curJ) in dic:
                    dfs(i + curI, j + curJ)
            
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in dic:
                    dfs(i, j)
                    total += 1

        return total

        



        
