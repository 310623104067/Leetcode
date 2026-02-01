# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        val = root.val

        def dfs(node):
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)