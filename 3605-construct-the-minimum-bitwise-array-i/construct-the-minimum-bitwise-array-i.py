class Solution(object):
    def minBitwiseArray(self, nums):
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
                continue

            x = 0
            while True:
                if (x | (x + 1)) == n:
                    res.append(x)
                    break
                x += 1
        return res
