class Solution:
    def longestUnivaluePath(self, root):
        # Initialize a variable to store the maximum length of univalue path found
        max_length = 0
        
        # Helper function to perform Depth-First Search (DFS)
        # It calculates the longest univalue path for each node
        def dfs(node):
            nonlocal max_length  # Allow modification of the max_length variable outside the function
            
            # Base case: If the node is None (empty), return 0
            if not node:
                return 0
            
            # Recursively calculate the length of the univalue path for the left and right subtrees
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            
            # Initialize the length of arrows (the path that can extend from the current node)
            left_arrow = right_arrow = 0
            
            # Check if the left child exists and has the same value as the current node
            # If yes, increase the left_arrow by 1 to indicate a continuation of the univalue path
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            
            # Similarly, check if the right child exists and has the same value as the current node
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            
            # Update max_length with the largest path found so far
            # This combines the left and right paths extending from the current node
            max_length = max(max_length, left_arrow + right_arrow)
            
            # Return the longest single path (either left or right) that can continue from the current node
            return max(left_arrow, right_arrow)
        
        # Start the DFS traversal from the root node
        dfs(root)
        
        # Return the maximum length of univalue paths found
        return max_length
