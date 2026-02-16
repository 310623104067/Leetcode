class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            jump = nums[i]
            target = (i + jump + n) % n
            result[i] = nums[target]
        
        return result
