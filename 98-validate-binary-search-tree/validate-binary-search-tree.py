# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.res = []
#         self.inorder(root)    
#         for i in range(len(self.res)-1):
#             if self.res[i]>=self.res[i+1]:
#                 return False
#         return True
        
#     def inorder(self,root):
#         if root:
#             self.inorder(root.left)
#             self.res.append(root.val)
#             self.inorder(root.right)

#Solution 2
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high):
            if not root:
                return True
            
            if low < root.val < high:
                return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
            else:
                return False

        return dfs(root, float("-inf"),float("inf"))

    


        

