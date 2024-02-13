#check number is a palindrome using recursion
def palindrome(n):#function to check if a number is a palindrome
    if len(n)==1 or len(n)==0:#base case
        return True#returning True if the number has only one digit or no digit
    else:
        if n[0]==n[-1]:#checking if the first and last digit are same
            return palindrome(n[1:-1])#returning the result of the number without the first and last digit
        else:
            return False#returning False if the first and last digit are not same
        
# check string is a palindrome using recursion
def palindrome_string(s):#function to check if a string is a palindrome
    if len(s)==1 or len(s)==0:#base case
        return True#returning True if the string has only one character or no character
    else:
        if s[0]==s[-1]:#checking if the first and last character are same
            return palindrome_string(s[1:-1])#returning the result of the string without the first and last character
        else:
            return False#returning False if the first and last character are not same
        #test the function