from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])
        ans = float("-inf")

        # Make cols the smaller dimension
        if rows > cols:
            matrix = [list(x) for x in zip(*matrix)]
            rows, cols = cols, rows

        for left in range(cols):
            rowSum = [0] * rows

            for right in range(left, cols):
                for r in range(rows):
                    rowSum[r] += matrix[r][right]

                prefix = [0]
                cur = 0

                for x in rowSum:
                    cur += x

                    # Need previous prefix >= cur - k
                    i = bisect_left(prefix, cur - k)

                    if i < len(prefix):
                        ans = max(ans, cur - prefix[i])

                    insort(prefix, cur)

                    if ans == k:
                        return k

        return ans