from collections import deque

class Solution:
    def possibleBipartition(self, n, dislikes):
        graph = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [-1] * (n + 1)

        for i in range(1, n + 1):
            if color[i] != -1:
                continue

            color[i] = 0
            q = deque([i])

            while q:
                u = q.popleft()

                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

                    elif color[v] == color[u]:
                        return False

        return True