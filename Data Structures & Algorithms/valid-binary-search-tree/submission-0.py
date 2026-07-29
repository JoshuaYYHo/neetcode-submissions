# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, left, right):
            
            # We know we executed the recursive process correctly
            if not node:
                return True

            if not (node.val < right and node.val > left):

                return False

            return (traverse(node.left, left, node.val) and 
            traverse(node.right, node.val, right))


        return traverse(root, float("-inf"), float("inf"))
            

        



        