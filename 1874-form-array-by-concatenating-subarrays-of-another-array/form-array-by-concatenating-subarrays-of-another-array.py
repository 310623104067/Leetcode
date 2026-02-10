class Solution:
    def canChoose(self, groups, nums):
        i = 0  # pointer in nums
        
        for group in groups:
            found = False
            while i + len(group) <= len(nums):
                if nums[i:i+len(group)] == group:
                    i += len(group)
                    found = True
                    break
                i += 1
            if not found:
                return False
        
        return True
