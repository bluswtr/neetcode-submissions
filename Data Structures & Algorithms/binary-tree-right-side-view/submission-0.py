# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

            # implement level order BFS traversal 
            # for each level, append rightmost element to output
            queue = deque()
            queue.append(root)
            res = []

            while queue:
                l = len(queue)

                for i in range(0,l):
                    node = queue.popleft()
                    if i == l - 1: # if we've reached the last element
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            return res

