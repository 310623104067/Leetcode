class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        
        # quick check
        if desiredTotal <= 0:
            return True
        
        total = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total < desiredTotal:
            return False
        
        memo = {}
        
        def dfs(used, target):
            if used in memo:
                return memo[used]
            
            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << i
                
                if used & mask == 0:
                    # if picking i wins immediately OR opponent loses
                    if i >= target or not dfs(used | mask, target - i):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False
        
        return dfs(0, desiredTotal)