# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, targetSum, currSum):
            if not root:
                return False
            currSum += root.val
            if root.left is None and root.right is None and targetSum == currSum:
                return True
            if helper(root.left, targetSum, currSum):
                return True
            if helper(root.right, targetSum, currSum):
                return True
            currSum -= root.val
            return False
        
        return helper(root, targetSum, 0)
            