# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # [[1]]
        queue = deque()
        queue.append(root)

        while queue:
            l = len(queue) # l = 2, queue = [3,4,5]
            temp = [] # [2,3]
            
            for _ in range(0,l): 
                node = queue.popleft() # 1
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if len(temp) > 0:
                res.append(temp)

        return res