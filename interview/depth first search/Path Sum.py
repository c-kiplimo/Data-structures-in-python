class Solution:
    def pathSum(self, root, target):
        # Base case: If the current node is None, the path doesn't exist, return False
        if root is None:
            return False
       
        # If we reach a leaf node (no left or right children), check if the current node's value equals the target
        if not root.left and not root.right:
            return target == root.val
        
        # Subtract the current node's value from the target for further checks down the path
        target -= root.val

        # Recursively check if either the left or right subtree has a valid path that adds up to the target
        # Returns True if any path in either subtree matches the target
        return self.pathSum(root.left, target) or self.pathSum(root.right, target)
