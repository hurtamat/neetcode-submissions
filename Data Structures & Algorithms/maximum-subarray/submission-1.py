class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = nums[0]
        curSum = 0

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0

            curSum += nums[i]

            if curSum > best:
                best = curSum

        return best