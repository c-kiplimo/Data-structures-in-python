def longestSubstringWithoutRepeat(s):
  # Dictionary to store the frequency of characters in the current window
  seen = {}
  # Variable to keep track of the maximum length of the substring without repeating characters
  max_length = 0
  # Start pointer for the sliding window
  start = 0

  # Iterate over each character in the string using the end pointer
  for end in range(len(s)):
    # Increment the frequency of the current character in the window
    seen[s[end]] = seen.get(s[end], 0) + 1

    # If the frequency of the current character is greater than 1,
    # it means there's a repeating character in the current window
    while seen[s[end]] > 1:
      # Decrease the frequency of the character at the start pointer
      seen[s[start]] -= 1
      # Move the start pointer to the right to reduce the window size
      start += 1

    # Update the maximum length if the current window size is greater
    max_length = max(max_length, end - start + 1)

  # Return the maximum length of the substring without repeating characters
  return max_length
