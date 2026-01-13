# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            leftmax = max(leftmax, 0)

            rightmax = dfs(root.right)
            rightmax = max(rightmax, 0)

            self.res = max(self.res, root.val + leftmax + rightmax)

            return root.val + max(leftmax, rightmax) 
        
        dfs(root)
        return self.res
            