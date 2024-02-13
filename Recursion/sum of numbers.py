# find sum on n natural numbers using recursion
def sum_natural(n):#function to find the sum of n natural numbers
    if n==1:#base case
        return 1#returning 1 if n is 1
    else:
        return n+sum_natural(n-1)#returning the sum of n and the sum of n-1
n=5
print(sum_natural(n))

#sum of elements of a list using recursion
def sum_list(L):#function to find the sum of elements of a list
    if len(L)==1:#base case
        return L[0]#returning the number if the list has only one element
    else:
        return L[0]+sum_list(L[1:])#returning the sum of the first element and the sum of the rest of the list