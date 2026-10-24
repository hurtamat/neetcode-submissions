class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        present = set()
        for num in nums:
            present.add(num)
        
        start = {}
        for num in present:
            if num - 1 in present:
                continue
            start[num] = 1

        print(f"{present}")
        print(f"{start}")

        best = 1
        for num in start:
            i = num
            while True:
                i = i+1
                if i in present:
                    start[num] += 1
                else:
                    if start[num] > best:
                        best = start[num]
                    break
        
        return best
        

            


        