class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                cur = prices[j] - prices[i]
                best = cur if cur > best else best
        
        return best