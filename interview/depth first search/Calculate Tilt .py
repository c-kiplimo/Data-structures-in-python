class Solution:
    def calculateTilt(self, root):
        # Initialize a variable to store the overall tilt of the tree
        tilt = 0
        
        # Helper function to perform depth-first search (DFS) and calculate tilt recursively
        def dfs(node):
            nonlocal tilt  # Allows access to the tilt variable defined outside this function
            
            # Base case: If the current node is None, return 0
            if not node:
                return 0

            # Recursively compute the sum of values in the left subtree
            left = dfs(node.left)
            
            # Recursively compute the sum of values in the right subtree
            right = dfs(node.right)
            
            # Calculate the tilt of the current node (absolute difference between left and right subtree sums)
            tilt += abs(left - right)
            
            # Return the total sum of the current subtree (including the current node's value)
            return left + right + node.val
        
        # Start the DFS traversal from the root node
        dfs(root)
        
        # Return the total tilt of the tree
        return tilt
