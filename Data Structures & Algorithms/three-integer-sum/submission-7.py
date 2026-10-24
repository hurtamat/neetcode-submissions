class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()

        
        ret = set()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ret.add((nums[i], nums[l], nums[r]))
                    l+= 1
                    r-= 1
                elif total < 0:
                    l+= 1
                else:
                    r-= 1
            
        retList = []
        for comb in ret:
            retList.append(comb)

        return retList

        
        
        