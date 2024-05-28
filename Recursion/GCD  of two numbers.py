#finding gcd of two numbers using recursion
def gcd(a,b):#function to find the gcd of two numbers
    if b==0:#base case
        return a#returning a if b is 0
    else:
        return gcd(b,a%b)#returning the gcd of b and a%b

