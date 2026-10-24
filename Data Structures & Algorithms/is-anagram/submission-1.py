class Solution:
    def fillAmount(self, s) -> dict:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        return self.fillAmount(s) == self.fillAmount(t)