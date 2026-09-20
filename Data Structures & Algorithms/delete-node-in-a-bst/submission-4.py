# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def findmin(self,root):
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            # key == root.val
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                small = self.findmin(root.right)
                root.val = small
                root.right = self.deleteNode(root.right,small)

        return root



        