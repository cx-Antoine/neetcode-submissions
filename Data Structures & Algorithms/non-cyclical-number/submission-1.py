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
            n = squaredigits(n) #Value reassigned to the squareddigit result for                                further comparison
        
        return n == 1



    