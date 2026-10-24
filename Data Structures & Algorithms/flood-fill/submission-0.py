class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return []
        
        m = len(image)
        n = len(image[0])

        q = deque()
        done = set()

        q.append([sr, sc])

        while q:
            x, y = q.popleft()
            if (x, y) in done:
                continue

            if x+1 < m and image[x + 1][y] == image[x][y] and (x+1, y) not in done:
                q.append([x+1, y])
            if y+1 < n and image[x][y + 1] == image[x][y] and (x, y+1) not in done:
                q.append([x, y+1])
            if x-1 >= 0 and image[x - 1][y] == image[x][y] and (x-1, y) not in done:
                q.append([x-1, y])
            if y-1 >= 0 and image[x][y - 1] == image[x][y] and (x, y-1) not in done:
                q.append([x, y-1])

            image[x][y] = color
            done.add((x, y))

        return image

            



        