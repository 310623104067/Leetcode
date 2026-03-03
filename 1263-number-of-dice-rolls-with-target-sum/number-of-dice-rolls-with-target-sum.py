class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for _ in range(n):
            new_dp = [0] * (target + 1)
            
            for t in range(1, target + 1):
                for face in range(1, k + 1):
                    if t - face >= 0:
                        new_dp[t] += dp[t - face]
            
            dp = [x % MOD for x in new_dp]
        
        return dp[target]