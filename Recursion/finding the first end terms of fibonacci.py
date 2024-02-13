# finding the n terms of fibonacci series using recursion also known as rabbit problem
def fibonacci(n):#function to find the nth term of fibonacci series
    if n==1:#base case
        return 0#returning 0 if n is 1
    elif n==2:#base case
        return 1#returning 1 if n is 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)#returning the sum of the n-1th and n-2th term