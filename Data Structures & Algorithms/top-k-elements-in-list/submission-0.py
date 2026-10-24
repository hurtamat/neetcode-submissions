class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = {}

        for num in nums:
            amount[num] = amount.get(num, 0) + 1

        top = []
        for i in range(k):
            top.append([-1, 0])
            for key, value in amount.items():
                if value >= top[i][0]:
                    top[i] = (value, key)
            amount.pop(top[i][1])

        print(f"{top}")

        ret = []
        for i in range(len(top)):
            ret.append(top[i][1])

        return ret
        


        
        
        