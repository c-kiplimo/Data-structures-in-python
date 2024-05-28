class Solution(object):
    def mergeAlternately(self, word1, word2):
        # Initialize an empty string
        result = ""
        # Loop through the length of the shorter string
        for i in range(min(len(word1), len(word2))):
            # Append the ith character of the first string to the result
            result += word1[i]
            # Append the ith character of the second string to the result
            result += word2[i]
        # Append the remaining characters of the longer string to the result
        result += word1[len(word2):] + word2[len(word1):]
        return result