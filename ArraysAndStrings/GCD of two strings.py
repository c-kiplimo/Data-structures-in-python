class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Check if the two strings are equal
        if str1 + str2 != str2 + str1: 
            return ""
        # Find the greatest common divisor of the lengths of the two strings
        return str1[:self.gcd(len(str1), len(str2))]  
    
# Function to find the greatest common divisor of two strings
    def gcd(self, a, b):#function to find the gcd of two numbers
        if b == 0:#base case
            return a#returning a if b is 0
        return self.gcd(b, a % b)#returning the gcd of b and a%b    