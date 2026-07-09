# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Compute max gain from left and right subtrees
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path sum through this node
            current_path_sum = node.val + left_gain + right_gain

            # Update global maximum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return max gain if continuing upward
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum
