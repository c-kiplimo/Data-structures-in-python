class Solution:
    def characterReplacement(self, s, k):
        # Dictionary to keep track of the frequency of each character in the current window
        state = {}
        
        # Variable to store the maximum frequency of any single character within the current window
        max_freq = 0
        
        # Variable to store the length of the longest valid window found
        max_length = 0
        
        # Start index of the current window
        start = 0

        # Iterate over each character in the string with the `end` pointer
        for end in range(len(s)):
            # Update the frequency count of the current character `s[end]`
            state[s[end]] = state.get(s[end], 0) + 1
            
            # Update the maximum frequency of any character in the current window
            max_freq = max(max_freq, state[s[end]])

            # If the current window size minus the maximum frequency of a character is greater than `k`,
            # it means we need to make more than `k` replacements to make all characters in the window the same
            # Therefore, we need to shrink the window from the left
            if k + max_freq < end - start + 1:
                # Decrease the frequency of the character at the `start` index
                state[s[start]] -= 1
                # Move the `start` pointer to the right to reduce the window size
                start += 1

            # Update the maximum length of the window found so far
            max_length = max(max_length, end - start + 1)

        # Return the length of the longest window where at most `k` replacements are needed
        return max_length
