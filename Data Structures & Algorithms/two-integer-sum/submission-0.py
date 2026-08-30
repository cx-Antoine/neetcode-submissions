class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numindex = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numindex:
                return [numindex[difference], i]
            else:
                numindex[num] = i