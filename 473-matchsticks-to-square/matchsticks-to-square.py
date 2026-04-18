class Solution(object):
    def makesquare(self, matchsticks):
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        
        sides = [0] * 4
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    
                    if backtrack(i + 1):
                        return True
                    
                    sides[j] -= matchsticks[i]
                
                # pruning: avoid same states
                if sides[j] == 0:
                    break
            
            return False
        
        return backtrack(0)