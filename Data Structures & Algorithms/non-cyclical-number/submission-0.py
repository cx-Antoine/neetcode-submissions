class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def squaredigits(n) -> int:
            res = 0
            for digit in str(n):
                res += int(digit) ** 2
            return res
        

        while n != 1 and n not in seen:
            seen.add(n)
            n = squaredigits(n)
        
        return n == 1



    