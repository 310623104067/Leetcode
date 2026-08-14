import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]

        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        dist = [float('inf')] * n
        dist[0] = 0

        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, cnt in graph[u]:
                nd = d + cnt + 1

                if nd < dist[v] and nd <= maxMoves:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        ans = sum(d <= maxMoves for d in dist)

        for u, v, cnt in edges:
            a = maxMoves - dist[u] if dist[u] <= maxMoves else 0
            b = maxMoves - dist[v] if dist[v] <= maxMoves else 0
            ans += min(cnt, a + b)

        return ans