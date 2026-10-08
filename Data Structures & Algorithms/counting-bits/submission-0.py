class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [] * (n + 1)
        for i in range(0, n + 1):
            count = 0
            num = i
            while num != 0:
                count = count + (num & 1)
                num = num >> 1
            output.append(count)
        return output
            
        