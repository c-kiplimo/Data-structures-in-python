class Solution:
    def pathSum(self, root, target):
        # Helper function that performs a Depth-First Search (DFS) on the tree
        # node: current node in the traversal
        # target: remaining sum we are looking for
        # path: current path of nodes leading to the target sum
        def dfs(node, target, path):
            # Base case: If the node is None (end of path), return
            if not node:
                return
            
            # Add the current node's value to the path
            path.append(node.val)
            
            # Check if it's a leaf node (no children)
            if not node.left and not node.right:
                # If the leaf node's value equals the target, we found a valid path
                if node.val == target:
                    # Append a copy of the current path to the result
                    result.append(path[:])  # path[:] creates a copy of the path
            
            # Recursively explore the left subtree, reducing the target by the current node's value
            dfs(node.left, target - node.val, path)
            # Recursively explore the right subtree, reducing the target by the current node's value
            dfs(node.right, target - node.val, path)
            
            # After exploring both subtrees, remove the current node (backtracking)
            path.pop()

        # List to store all the valid paths that sum up to the target
        result = []
        
        # Start the DFS traversal from the root node, with an empty path
        dfs(root, target, [])
        
        # Return the list of valid paths
        return result
    


    from collections import defaultdict


### PATH III
class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(node, currSum):
            if not node:
                return 0

            # Compute current prefix sum
            currSum += node.val

            # Check if there exists a prefix sum that gives the targetSum
            count = prefixSumCount[currSum - targetSum]

            # Update prefixSumCount
            prefixSumCount[currSum] += 1

            # Recur on left and right children
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            # Backtrack: remove current sum from prefixSumCount
            prefixSumCount[currSum] -= 1

            return count

        # Hashmap to store prefix sum frequencies
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1  # Base case: to handle when a path equals targetSum exactly

        return dfs(root, 0)


