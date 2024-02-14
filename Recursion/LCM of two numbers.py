#lcm of two numbers
def lcm(a,b):#function to find the lcm of two numbers
    def gcd(a,b):#function to find the gcd of two numbers
        if b==0:#base case
            return a#returning a if b is 0
        else:
            return gcd(b,a%b)#returning the gcd of b and a%b
    return (a*b)//gcd(a,b)#returning the lcm of a and b

print(lcm(4,6))