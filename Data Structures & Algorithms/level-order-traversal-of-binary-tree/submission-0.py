# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            levellength = len(queue)
            curr = []
            for i in range(levellength):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)

                curr.append(queue[0].val)
                queue.popleft()
            result.append(curr)

        return result
