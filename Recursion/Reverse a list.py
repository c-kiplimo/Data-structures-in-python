def reverse(L):
    if (len(L))==1:
        return L
    else:
        return ([L[-1]]+reverse(L[:-1]))
    L = [1,2,3,4,5]
    reverse(L)