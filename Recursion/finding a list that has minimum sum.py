# Given a list of lists, fnd the list having a minimum sum. 
def find_min_sum(L):#function to find the list having minimum sum
    if len(L)==1:#base case
        return L[0]#returning the list if it has only one element
    rest=find_min_sum(L[1:])#finding the list having minimum sum in the rest of the list
    return (L[0] if sum(L[0])<sum(rest) else rest)#returning the list having minimum sum in the list