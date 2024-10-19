class Solution:
    def maxDepth(self, root):
        # Base case: If the current node is None, the depth is 0
        if root is None:
            return 0

        # Recursive call to calculate the depth of the left subtree
        left = self.maxDepth(root.left)
        
        # Recursive call to calculate the depth of the right subtree
        right = self.maxDepth(root.right)

        # Return the maximum of the left and right depths, plus 1 to account for the current node
        return max(left, right) + 1
