class Solution:
    # Method to search for 'target' in a rotated sorted array 'nums'
    def search(self, nums, target):
        # If the array is empty, return -1 as target cannot be found
        if not nums:
            return -1

        # Initialize the search boundaries: 'left' starts at the beginning, 'right' at the end of the array
        left, right = 0, len(nums) - 1

        # Perform binary search until 'left' exceeds 'right'
        while left <= right:
            # Find the midpoint index
            mid = (left + right) // 2
            
            # If the target is at the midpoint, return 'mid' index
            if nums[mid] == target:
                return mid
            
            # Determine if the left half of the array is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    # Narrow the search to the left half
                    right = mid - 1
                else:
                    # Otherwise, search in the right half
                    left = mid + 1
            
            # If the left half isn't sorted, then the right half must be sorted
            else:
                # Check if the target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    # Narrow the search to the right half
                    left = mid + 1
                else:
                    # Otherwise, search in the left half
                    right = mid - 1
        
        # If the target isn't found, return -1
        return -1
