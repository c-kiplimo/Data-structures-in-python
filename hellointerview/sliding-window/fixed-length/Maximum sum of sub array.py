def max_subarray_sum(nums, k):
    # Initialize `max_sum` to keep track of the maximum sum of any subarray of size `k`
    max_sum = 0
    
    # Initialize `state` to keep track of the current sum of the window
    state = 0
    
    # `start` will be used to indicate the beginning index of the sliding window
    start = 0

    # Iterate over each element in the `nums` list with the `end` pointer
    for end in range(len(nums)):
        # Add the current element to the `state` (current window sum)
        state += nums[end]

        # Check if the current window size is exactly `k`
        if end - start + 1 == k:
            # Update `max_sum` to be the maximum of its current value or the current window's sum (`state`)
            max_sum = max(max_sum, state)
            
            # Subtract the element at the `start` index from `state` to slide the window
            state -= nums[start]
            
            # Move the `start` pointer to the right to shrink the window
            start += 1

    # Return the maximum sum found for any subarray of size `k`
    return max_sum
