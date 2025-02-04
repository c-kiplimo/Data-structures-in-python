class Solution:
    def largestRectangleArea(self, heights):
        # Initialize a stack to store the indices of the histogram bars
        stack = []
        # Variable to store the maximum area
        max_area = 0
        # Pointer to iterate over the heights
        i = 0

        # Loop through the histogram bars
        while i < len(heights):
            # If the current bar is higher or equal to the bar at the top of the stack
            # or the stack is empty, push the current index to the stack
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                # Pop the top index from the stack (the bar we're calculating the area for)
                top = stack.pop()
                # Calculate the right boundary of the rectangle (current index - 1)
                right = i - 1
                # Calculate the left boundary of the rectangle (either the previous index in the stack or -1 if the stack is empty)
                left = stack[-1] if stack else -1
                # Calculate the area for the popped bar (height[top] * width between left and right)
                area = heights[top] * (right - left)
                # Update the maximum area
                max_area = max(max_area, area)

        # Process the remaining bars in the stack after we've finished iterating through heights
        while stack:
            # Pop the top index from the stack
            top = stack.pop()
            # Calculate the width for the remaining bars
            width = i - stack[-1] - 1 if stack else i
            # Calculate the area for the popped bar
            area = heights[top] * width
            # Update the maximum area
            max_area = max(max_area, area)

        # Return the largest rectangle area
        return max_area
