from bisect import bisect_right, insort

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        arr = []
        ans = 0

        for a, b in zip(nums1, nums2):
            x = a - b
            ans += bisect_right(arr, x + diff)
            insort(arr, x)

        return ans