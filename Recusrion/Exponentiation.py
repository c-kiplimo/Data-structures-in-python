def power(a,b):
    if(b==0):
        return 1
    else:
        return (a*pow(a,b-1))

    # also it can be implemented as
def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
 