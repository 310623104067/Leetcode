class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        MOD = 10**9 + 7
        
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        
        dp[0][0][0] = 1
        
        for i in range(n):
            for a in range(2):
                for l in range(3):
                    
                    val = dp[i][a][l]
                    
                    if val == 0:
                        continue
                    
                    # Add P
                    dp[i+1][a][0] = (dp[i+1][a][0] + val) % MOD
                    
                    # Add A
                    if a == 0:
                        dp[i+1][1][0] = (dp[i+1][1][0] + val) % MOD
                    
                    # Add L
                    if l < 2:
                        dp[i+1][a][l+1] = (dp[i+1][a][l+1] + val) % MOD
        
        ans = 0
        
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[n][a][l]) % MOD
        
        return ans