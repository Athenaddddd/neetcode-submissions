# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        result =[]
        
        if root:
                queue.append(root)
        
        while len(queue) > 0:
            levellength = len(queue)

            for i in range(levellength):

                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)

                if i == levellength - 1:
                    result.append(queue[0].val)
                    queue.popleft()          
                else:
                    queue.popleft()

        return result

