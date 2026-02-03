# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def dfs(node):
            if not node:
                return(0,0)
            ls,lc=dfs(node.left)
            rs,rc=dfs(node.right)
            sums=ls+rs+node.val
            cnt=lc+rc+1
            if sums//cnt==node.val:
                self.ans+=1
            return (sums,cnt)
        dfs(root)
        return self.ans
