# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse(node, level):
            if not node:
                return 

            if level == len(result):
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)

            traverse(node.left, level+1)
            traverse(node.right, level+1)

        traverse(root, 0)

        return result