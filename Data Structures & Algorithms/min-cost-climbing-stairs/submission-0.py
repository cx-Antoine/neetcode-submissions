class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = (len(cost) + 1)
        dp = [None] * n
        dp[0] = 0 # no cost starting at 0 or 1
        dp[1] = 0

        for i in range(2, n): # start the costs after 2 and add the min up to that point and then the cost of moving from that point
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n - 1] #because n = lenght of cost = 1 so the top will be n-1