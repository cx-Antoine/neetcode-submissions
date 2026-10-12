class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) #The number the normal index can never reach, we need it to XOR out

        for i in range(len(nums)):
            res = res ^ nums[i] ^ i

        return res

        
        