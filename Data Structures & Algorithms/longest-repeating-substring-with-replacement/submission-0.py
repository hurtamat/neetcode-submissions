class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dic = {}
        res = 0

        l = 0
        n = len(s)

        for r in range(n):
            dic[s[r]] = dic.setdefault(s[r], 0) + 1

            while (max(dic.values()) + k < r - l + 1):
                if dic[s[l]] == 1:
                    dic.pop(s[l])
                else:
                    dic[s[l]] -= 1
                l+= 1

            if res < r - l + 1:
                res = r - l + 1

        return res
                    



        