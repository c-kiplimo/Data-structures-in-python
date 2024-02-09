import time


def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

tic = time.time()
print(fibonacci(35))
toc = time.time()
diff = toc-tic
print(diff)

#second implementation
def fibonacci(n):
    L=[]
    L.append(1)
    L.append(1)
    for i in range(2,n):
        L.append(L[i-1]+L[i-2])
    return L[n-1]

tic = time.time()
print(fibonacci(35))
toc = time.time()
diff = toc-tic
print(diff)