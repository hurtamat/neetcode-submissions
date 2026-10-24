class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for ch in s:
            if ch.isalpha():
                chars.append(ch.lower())
            elif ch.isdigit():
                chars.append(ch)

        right = len(chars) - 1
        left = 0

        while right >= left:
            if chars[right] != chars[left]:
                return False
            else:
                right-= 1
                left += 1
        
        return True
        