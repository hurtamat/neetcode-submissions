class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        dic2 = {}
        
        if not s1 or not s2 or len(s2) < len(s1):
            return False

        
        window_size = len(s1)

        for i in range(window_size):
            dic1[s1[i]] = dic1.get(s1[i], 0) + 1
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        for r in range(window_size, len(s2)):

            if dic1 == dic2:
                return True

            print(f"dic1: {dic1} dic2: {dic2}")

            dic2[s2[r]] = dic2.get(s2[r], 0) + 1

            l = r - window_size
            if dic2[s2[l]] == 1:
                del dic2[s2[l]]
            else:
                dic2[s2[l]] -= 1

        if dic1 == dic2:
                return True

        return False

            

            