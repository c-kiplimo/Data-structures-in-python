class Solution:
    def maxScore(self, cards, k):
        # Calculate the total sum of all elements in the `cards` list
        total = sum(cards)
        
        # If `k` is greater than or equal to the length of `cards`, return the total sum
        if k >= len(cards):
            return total

        # `state` will keep track of the sum of the elements in the current window
        state = 0
        
        # `max_points` will store the maximum score possible by selecting exactly `k` cards
        max_points = 0
        
        # `start` is the start index of the sliding window
        start = 0

        # Iterate over each element in the `cards` list with the `end` pointer
        for end in range(len(cards)):
            # Add the current element to the `state` (current window sum)
            state += cards[end]
            
            # Check if the current window size is exactly `len(cards) - k`
            if end - start + 1 == len(cards) - k:
                # Update `max_points` to be the maximum of current `max_points` and total sum minus `state`
                max_points = max(total - state, max_points)
                
                # Subtract the element at the `start` index from `state` to slide the window
                state -= cards[start]
                
                # Move the `start` pointer to the right to shrink the window
                start += 1
        
        # Return the maximum score possible with exactly `k` cards
        return max_points
