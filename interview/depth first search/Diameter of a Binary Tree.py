class Solution:
    def maxDiameter(self, root):
        # Initialize a variable to store the maximum diameter of the tree
        max_ = 0
        
        # Helper function to perform depth-first search (DFS) and calculate the diameter
        def dfs(node):
            nonlocal max_  # Allows access to the max_ variable defined outside this function
            
            # Base case: If the current node is None, return 0 (no height)
            if not node:
                return 0

            # Recursively compute the height of the left subtree
            left = dfs(node.left)
            
            # Recursively compute the height of the right subtree
            right = dfs(node.right)
            
            # Update the maximum diameter if the current diameter (left + right) is larger than the current max
            max_ = max(max_, left + right)
            
            # Return the height of the current subtree (1 + the maximum of left or right subtree heights)
            return max(left, right) + 1
        
        # Start DFS traversal from the root node
        dfs(root)
        
        # Return the maximum diameter of the tree
        return max_
