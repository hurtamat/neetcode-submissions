class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sl1 = []
        sl2 = []
        n = len(s2)

        if n < len(s1):
            return False

        if not s1 or not s1:
            return False



        for i in range(len(s1)):
            sl1.append(s1[i])

        for i in range(n):
            sl2.append(s2[i])

        

        sl1.sort()

        for i in range(n - len(sl1) + 1):
            cur = sorted(sl2[i:i+len(sl1)])

            if cur == sl1:
                return True
        
        return False
        