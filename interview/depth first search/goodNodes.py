class Solution(object):
    def goodNodes(self, root):
        # Helper function to perform DFS and count good nodes
        def dfs(node, max_val):
            if not node:
                return 0  # If node is None, return 0
            
            # Check if the current node is a good node
            good = 1 if node.val >= max_val else 0
            
            # Update the maximum value for the next level
            max_val = max(max_val, node.val)
            
            # Recur for left and right children
            left_good = dfs(node.left, max_val)
            right_good = dfs(node.right, max_val)
            
            return good + left_good + right_good
        
        # Start DFS from root node with its value as the max_val
        return dfs(root, root.val)
