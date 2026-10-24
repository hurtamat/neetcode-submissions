class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book = {}
        for num in nums:
            if num in book:
                return True
            else:
                book[num] = True
        
        return False
            
        