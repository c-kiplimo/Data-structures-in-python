#reverse vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')#set of vowels
        s = list(s)#convert the string to a list
        i, j = 0, len(s) - 1#initialize i to 0 and j to the length of the string - 1
        while i < j:#loop through the string
            if s[i] in vowels and s[j] in vowels:#if the characters at i and j are vowels
                s[i], s[j] = s[j], s[i]#swap the characters
                i += 1#increment i by 1
                j -= 1#decrement j by 1
            if s[i] not in vowels:#if the character at i is not a vowel
                i += 1#increment i by 1
            if s[j] not in vowels:#if the character at j is not a vowel
                j -= 1#decrement j by 1
        return ''.join(s)#return the string
# another simple solution
