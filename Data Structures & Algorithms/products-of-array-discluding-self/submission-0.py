class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nulls = []
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                nulls.append(i)
            else:
                total = total*nums[i]

        ret = []

        for i in range(len(nums)):
            if not nulls:
                ret.append(int(total / nums[i]))
            elif len(nulls) == 1 and nulls[0] == i:
                ret.append(total)
            else:
                ret.append(0)
        return ret



        