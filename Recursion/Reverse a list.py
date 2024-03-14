def reverse(L):#function to reverse a list
    if (len(L))==1:#base case
        return L#returning the list if it has only one element
    else:
        return ([L[-1]]+reverse(L[:-1]))#returning the reverse of the list
    L = [1,2,3,4,5]
    reverse(L)


    #reverse a string
def reverse(s):#function to reverse a string
    if len(s)==1:#base case
        return s#returning the string if it has only one character
    else:
        return (s[-1]+reverse(s[:-1]))#returning the reverse of the string