class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charAmount = {}

        for char in ransomNote:
            if char in charAmount:
                charAmount[char] += 1
            else:
                charAmount[char] = 1

        
        for char in magazine:
            if char in charAmount:
                if charAmount[char] == 1:
                    charAmount.pop(char)
                else:
                    charAmount[char] -= 1
            
        if charAmount:
            return False
        else:
            return True

        