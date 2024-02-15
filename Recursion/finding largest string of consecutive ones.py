# Given a two-dimensional array of 0’s and 1’s. Find the largest string of 
# consecutive  ones.  These  consecutive  ones  may  be  present  horizontally, 
# vertically, or diagonally. 

def find_ones(L):#function to find the largest string of consecutive ones
    def find_ones_in_row(row):#function to find the largest string of consecutive ones in a row
        if len(row)==1:#base case
            return row[0]#returning the row if it has only one element
        rest=find_ones_in_row(row[1:])#finding the largest string of consecutive ones in the rest of the row
        return (row[0] if row[0]>rest else rest)#returning the largest string of consecutive ones in the row
    if len(L)==1:#base case
        return find_ones_in_row(L[0])#returning the row if it has only one element
    rest=find_ones(L[1:])#finding the largest string of consecutive ones in the rest of the list
    return (find_ones_in_row(L[0]) if find_ones_in_row(L[0])>rest else rest)#returning the largest string of consecutive ones in the list
L=[[1,1,0,1,1],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[1,1,1,1,1]]
print(find_ones(L))