def towerOfHanoi(num,source,aux,dest):#function to solve the tower of hanoi problem
    if num==1:#base case
        print("Move disk 1 from source",source,"to destination",dest)#printing the move
        return#returning if there is only one disk
    towerOfHanoi(num-1,source,aux,dest) #recursively calling the function to move n-1 disks from source to aux
    print("Move disk",num,"from source",source,"to destination",dest)
    towerOfHanoi(num-1,aux,dest,source)#recursively calling the function to move n-1 disks from aux to dest
towerOfHanoi(3,'A','B','C')