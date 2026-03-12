class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            
            gold = grid[r][c]
            grid[r][c] = 0
            
            max_gold = 0
            
            max_gold = max(max_gold, dfs(r+1,c))
            max_gold = max(max_gold, dfs(r-1,c))
            max_gold = max(max_gold, dfs(r,c+1))
            max_gold = max(max_gold, dfs(r,c-1))
            
            grid[r][c] = gold
            
            return gold + max_gold
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i,j))
        
        return ans