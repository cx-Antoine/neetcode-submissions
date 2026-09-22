class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        
        start = 0
        def backTrack(start):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backTrack(i + 1)
                current.pop()

        backTrack(0)
        return result