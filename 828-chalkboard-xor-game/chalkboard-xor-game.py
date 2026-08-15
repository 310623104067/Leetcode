class Solution:
    def xorGame(self, nums):
        x = 0

        for num in nums:
            x ^= num

        return x == 0 or len(nums) % 2 == 0