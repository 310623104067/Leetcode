class Solution(object):
    def loudAndRich(self, richer, quiet):
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for a, b in richer:
            graph[b].append(a)  # b → richer people
        
        n = len(quiet)
        ans = [-1] * n
        
        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            
            ans[x] = x
            
            for nei in graph[x]:
                candidate = dfs(nei)
                if quiet[candidate] < quiet[ans[x]]:
                    ans[x] = candidate
            
            return ans[x]
        
        for i in range(n):
            dfs(i)
        
        return ans