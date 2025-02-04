class Solution:
    def maxSum(self, nums, k):
        # Initialize `max_sum` to keep track of the maximum sum of any subarray of size `k`
        max_sum = 0
        
        # `start` will be used to indicate the beginning index of the sliding window
        start = 0
        
        # `state` keeps track of the frequency of each element within the current window
        state = {}
        
        # `curr_sum` keeps the sum of the current window
        curr_sum = 0

        # Iterate over each element in the `nums` list with the `end` pointer
        for end in range(len(nums)):
            # Add the current element to the `curr_sum` (current window sum)
            curr_sum += nums[end]
            
            # Update the frequency count of the current element in the `state` dictionary
            state[nums[end]] = state.get(nums[end], 0) + 1
            
            # Check if the current window size is exactly `k`
            if end - start + 1 == k:
                # If the number of unique elements in the window is exactly `k`, update `max_sum`
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)
                
                # Subtract the element at the `start` index from `curr_sum` to slide the window
                curr_sum -= nums[start]
                
                # Decrease the frequency count of the element that is being removed from the window
                state[nums[start]] -= 1
                
                # If the count of the element becomes zero, remove it from the `state` dictionary
                if state[nums[start]] == 0:
                    del state[nums[start]]
                
                # Move the `start` pointer to the right to shrink the window
                start += 1

        # Return the maximum sum found for any subarray of size `k` with exactly `k` unique elements
        return max_sum
