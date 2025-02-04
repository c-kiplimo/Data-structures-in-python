class Solution:
    # Define a method to find the minimum rate needed to harvest all apples within the given hours 'h'
    def minHarvestRate(self, apples, h):
        
        # Helper function to calculate the time required to harvest all apples at a given rate
        def time_taken(rate):
            time = 0  # Initialize total time required
            # For each orchard, calculate the hours needed to harvest apples at the specified rate
            for i in range(len(apples)):
                # Ceiling division to calculate time for current orchard
                time += (apples[i] + rate - 1) //rate
            return time  # Return the total time for the current rate

        # Initialize the search range for the rate: 
        # 'left' is the minimum rate, 'right' is the maximum apples in any orchard
        left, right = 1, max(apples)
        
        # Perform binary search to find the minimum feasible rate
        while left < right:
            # Calculate the midpoint rate to test
            mid = (left + right) // 2
            
            # If harvesting at 'mid' rate takes more time than allowed hours 'h'
            if time_taken(mid) > h:
                # Increase 'left' to search in the higher rate range
                left = mid + 1
            else:
                # Otherwise, search in the lower rate range by updating 'right'
                right = mid
                
        # 'left' will eventually hold the minimum rate that satisfies the condition
        return left
