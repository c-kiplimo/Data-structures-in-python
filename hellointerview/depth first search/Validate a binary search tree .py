class Solution:
    def validateBST(self, root):
        # Helper function to perform DFS (Depth-First Search) and validate the BST
        def dfs(node, left, right):
            # Base case: If the current node is None, we have reached a leaf or empty tree, so return True
            if not node:
                return True

            # Check if the current node's value violates the BST properties:
            # It must be greater than the allowed `left` bound and less than the `right` bound
            if not (left < node.val < right):
                return False

            # Recursively validate the left subtree:
            # - The current node's value becomes the new right bound for the left subtree
            # Recursively validate the right subtree:
            # - The current node's value becomes the new left bound for the right subtree
            return (dfs(node.left, left, node.val) and  # Left subtree: valid range is (left, node.val)
                    dfs(node.right, node.val, right))  # Right subtree: valid range is (node.val, right)

        # Start the DFS with the root node and set the initial boundaries to negative and positive infinity
        # This allows the root node to take any valid integer value
        return dfs(root, float('-inf'), float('inf'))
