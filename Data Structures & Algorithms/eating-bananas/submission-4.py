class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatPiles(piles: List[int], k) -> int:
            cur = 0
            for pile in piles:
                cur += (pile + k - 1) // k
            
            return cur
        
        if not piles:
            return 0

        top = max(piles)


        best = top
        
        l = 1
        r = top

        while l <= r:
            m = (l+r) // 2

            cur = eatPiles(piles, m)

            if cur > h:
                l = m + 1
            else:
                best = m
                r = m - 1
        
                

        return best



        


        