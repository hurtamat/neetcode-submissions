class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        best = 0
        leftMin = prices[0]
        leftMinList = []
        leftMinList.append(0)
        for i in range(1, len(prices)):
            leftMin = leftMin if leftMin < prices[i - 1] else prices[i - 1]
            leftMinList.append(leftMin)
        

        for i in range(1, len(prices)):
            best = best if best > prices[i] - leftMinList[i] else prices[i] - leftMinList[i]

        return best
        

        

            