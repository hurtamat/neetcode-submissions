class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            ret.append(f"{len(s)}|{s}")
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            delim_idx = s.find("|", i)
            
            length = int(s[i:delim_idx])
            
            word_start = delim_idx + 1
            word_end = word_start + length
            res.append(s[word_start:word_end])
            
            i = word_end

        return res


