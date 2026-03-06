# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        memo = {}
        
        def build(n):
            
            if n in memo:
                return memo[n]
            
            if n == 1:
                return [TreeNode(0)]
            
            res = []
            
            for left in range(1, n, 2):
                
                right = n - 1 - left
                
                leftTrees = build(left)
                rightTrees = build(right)
                
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            memo[n] = res
            return res
        
        return build(n)