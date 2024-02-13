def power(a,b):#function to find the power of a number
    if(b==0):#base case
        return 1#returning 1 if the power is 0
    else:
        return (a*pow(a,b-1))#returning the product of the number and the power of the number-1

    # also it can be implemented as
def factorial(n):#function to find the factorial of a number
    if(n==0):#base case
        return 1#returning 1 if the number is 0
    else:
        return n*factorial(n-1)#returning the product of the number and the factorial of the number-1
 