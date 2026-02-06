class Solution(object):
    def numSubmat(self, mat):
        m = len(mat)
        n = len(mat[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            stack = []
            count = [0] * n

            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    count[j] = count[prev] + heights[j] * (j - prev)
                else:
                    count[j] = heights[j] * (j + 1)

                stack.append(j)
                ans += count[j]

        return ans
