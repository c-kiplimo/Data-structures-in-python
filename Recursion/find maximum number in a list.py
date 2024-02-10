def find_max(L):
    if len(L)==1:
        return L[0]
    rest=find_max(L[1:])
    return (L[0] if L[0]>rest else rest)
L=[7,12,3,4,5]
print(find_max(L))