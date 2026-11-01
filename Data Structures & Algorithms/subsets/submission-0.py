class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []

        def back(curPath:List[int], index: int):
            if index >= len(nums):
                print(curPath)
                ret.append(list(curPath))
                return

            back(curPath, index + 1)
            curPath.append(nums[index])
            back(curPath, index + 1)

            curPath.pop()

            return
        
        

        back([], 0)

        return ret

            



        