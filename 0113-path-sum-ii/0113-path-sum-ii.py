# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        god_list = []
        curr_list = []

        def dfs(node, remaining_sum):
            if node is None:
                return

            curr_list.append(node.val)

            if not node.left and not node.right:
                if remaining_sum == node.val:
                    god_list.append(list(curr_list))
            else:
                dfs(node.left, remaining_sum - node.val)
                dfs(node.right, remaining_sum - node.val)

            curr_list.pop()

        dfs(root, targetSum)

        return god_list