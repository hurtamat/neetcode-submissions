class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        n = len(grid)
        m = len(grid[0])
        time = 0
        topTime = 0

        directions = ((1, 0),(0, 1) ,(-1, 0), (0, -1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j, time])
                    seen.add((i, j))

        while q:
            i, j, curTime = q.popleft()
            grid[i][j] = 2
            if curTime > topTime:
                topTime = curTime

            for d in directions:
                vi, vj = d
                if 0 <= i+vi < n and 0 <= j+vj < m and (i+vi, j+vj) not in seen and grid[i+vi][j+vj] == 1:
                    q.append([i + vi, j + vj, curTime + 1])
                    seen.add((i+vi, j+vj))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return topTime
                
            
            



        