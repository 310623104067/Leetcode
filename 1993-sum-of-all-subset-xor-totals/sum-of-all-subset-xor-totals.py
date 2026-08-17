class Solution:
    def subsetXORSum(self, nums):
        ans = [0]

        def dfs(i, xor):
            if i == len(nums):
                ans[0] += xor
                return

            dfs(i + 1, xor)
            dfs(i + 1, xor ^ nums[i])

        dfs(0, 0)
        return ans[0]