class Solution:
    dic = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.dic:
            return self.dic[n]


        total = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.dic[n] = total
        print(f"n: {n} total: {total}")
        return total