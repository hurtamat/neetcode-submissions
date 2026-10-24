class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            dic.setdefault("".join(sorted(strs[i])), []).append(strs[i])        
        
        return list(dic.values())



        


        