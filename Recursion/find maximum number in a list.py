def find_max(L):#function to find the maximum number in a list
    if len(L)==1:#base case
        return L[0]#returning the number if the list has only one element
    rest=find_max(L[1:])#finding the maximum number in the rest of the list
    return (L[0] if L[0]>rest else rest)#returning the maximum number in the list
L=[7,12,3,4,5]
print(find_max(L))