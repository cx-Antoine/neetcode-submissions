class Solution:
    def climbStairs(self, n: int) -> int:
        # return 0 if i is equal to n
        # 

        if n <= 1:
            return 1

        cache = [None] * (n + 1)
        cache[0] = 1
        cache[1] = 1

        for i in range(2, n+1):
            cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[n]