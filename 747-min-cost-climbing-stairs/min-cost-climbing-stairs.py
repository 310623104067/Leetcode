class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        if n==0:
            return 0
        if n==1:
            return cost[0]
        dp0=cost[0]
        dp1=cost[1]
        for i in range(2,n):
            res=cost[i]+min(dp0,dp1)
            dp0=dp1
            dp1=res
        return min(dp0,dp1)
        