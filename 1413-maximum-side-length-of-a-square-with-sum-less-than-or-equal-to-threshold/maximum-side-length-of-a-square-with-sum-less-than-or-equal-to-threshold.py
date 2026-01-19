class Solution(object):
    def maxSideLength(self, mat, threshold):
        m = len(mat)
        n = len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                pref[i + 1][j + 1] = mat[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j]

        def getsum(x1, y1, x2, y2):
            return pref[x2][y2] - pref[x1][y2] - pref[x2][y1] + pref[x1][y1]

        lo, hi = 0, min(m, n)
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            ok = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if getsum(i, j, i + mid, j + mid) <= threshold:
                        ok = True
                        break
                if ok:
                    break

            if ok:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
