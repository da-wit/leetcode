# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def findpath(root,path):
            if not root:
                return
            path += root.val
            if not root.left and not root.right:
                if path == targetSum:
                    return True
            return findpath(root.left,path) or findpath(root.right,path)
        
        return findpath(root,0)




