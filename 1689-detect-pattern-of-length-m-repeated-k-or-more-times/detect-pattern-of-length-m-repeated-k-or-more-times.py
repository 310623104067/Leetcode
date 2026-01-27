class Solution(object):
    def containsPattern(self, arr, m, k):
        n = len(arr)
        for i in range(n - m * k + 1):
            ok = True
            for j in range(m * (k - 1)):
                if arr[i + j] != arr[i + j + m]:
                    ok = False
                    break
            if ok:
                return True
        return False
