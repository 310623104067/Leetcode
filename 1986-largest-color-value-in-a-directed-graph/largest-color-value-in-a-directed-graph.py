from collections import deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        n = len(colors)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        ans = 0

        while q:
            node = q.popleft()
            visited += 1

            ans = max(ans, max(dp[node]))

            for nei in graph[node]:
                color_idx = ord(colors[nei]) - ord('a')

                for c in range(26):
                    add = 1 if c == color_idx else 0
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + add)

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if visited != n:
            return -1

        return ans