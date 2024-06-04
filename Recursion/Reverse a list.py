def reverse(L):#function to reverse a list
    if (len(L))==1:#base case
        return L#returning the list if it has only one element
    else:
        return ([L[-1]]+reverse(L[:-1]))#returning the reverse of the list
    L = [1,2,3,4,5]
    reverse(L)


    #reverse a string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # Split the string into words
        reversed_words = words[::-1]  # Reverse the list of words
        return ' '.join(reversed_words)  # Join the reversed words back into a string

# Example usage:
solution = Solution()
s = "hello world"
print(solution.reverseWords(s))  # Output: "world hello"
