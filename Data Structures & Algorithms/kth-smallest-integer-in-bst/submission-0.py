# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        # Traverse the tree and then build the list

        ls = []

        stack = [root]
        # use dfs pr bfs
        while stack:

            node = stack.pop()

            if node is None:
                continue
            
            ls.append(node.val)

            stack.append(node.left)
            stack.append(node.right)

        # Sort the list

        ls = sorted(ls)

        # Then return the kth item in the list

        return ls[k-1]