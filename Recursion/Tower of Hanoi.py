def towerOfHanoi(num,source,aux,dest):
    if num==1:
        print("Move disk 1 from source",source,"to destination",dest)
        return
    towerOfHanoi(num-1,source,aux,dest)
    print("Move disk",num,"from source",source,"to destination",dest)
    towerOfHanoi(num-1,aux,dest,source)
towerOfHanoi(3,'A','B','C')