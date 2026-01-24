class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        length = 1
        while length <= k:
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
            length += 1

        return -1
