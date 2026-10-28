class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        ret = 0

        window = set()

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            ret = max(ret, right - left + 1)

        return ret



        


        