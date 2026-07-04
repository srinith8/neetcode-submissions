# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        # The queue stores tuples: (node, level)
        q = collections.deque([(root, 0)])
        
        while q:
            node, level = q.popleft()
            
            # If 'res' doesn't have a sub-list for this level yet, create one
            if len(res) == level:
                res.append([])
                
            # Add the current node's value to its corresponding level list
            res[level].append(node.val)
            
            # Add children to the queue with an incremented level
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
                
        return res
        