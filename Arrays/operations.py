def fnd_max(arr, n):#function to find the maximum element in the array
    max1=0#variable to store the maximum element
    for i in range(1,n):#loop to traverse the array
      if(arr[i]>max1):#condition to check if the current element is greater than the maximum element
         max1=arr[i]#storing the current element in max1
    return(max1)

# Find minimum element in the array
def fnd_min(arr,n):
    min1=0#variable to store the minimum element
    for i in range(1,n):#loop to traverse the array
      if(arr[i]<min1):#condition to check if the current element is less than the minimum element
         min1=arr[i]#storing the current element in min1
    return(min1)

#Find sum of all elements in the array
def sum_arr(arr,n):
    sum1=0#variable to store the sum of all elements
    for i in range(n):#loop to traverse the array
      sum1+=arr[i]#adding the current element to sum1
    return(sum1)

#Find product of all elements in the array
def prod_arr(arr,n):
    prod=1#variable to store the product of all elements
    for i in range(n):#loop to traverse the array
      prod*=arr[i]#multiplying the current element to prod
    return(prod)

 
def linear_search(arr, n, item): #function to perform linear search
    flag=0 #variable to store the flag
    for i in range(n): #loop to traverse the array
       if(arr[i]==item):#condition to check if the current element is equal to the item
        print('Found at \t:',i)
        flag=1#setting the flag to 1
    if(flag==0):
       print('Not found')


#find mean of all elements in the array
def mean_arr(arr,n):
    sum1=0#variable to store the sum of all elements
    for i in range(n):#loop to traverse the array
      sum1+=arr[i]#adding the current element to sum1
    return(sum1/n)#returning the mean


# Find median of all elements in the array
def median_arr(arr,n):
    arr.sort()#sorting the array
    if(n%2==0):#condition to check if the number of elements in the array is even
        return((arr[n//2]+arr[n//2-1])/2)#returning the median of the two middle elements
    else:
        return(arr[n//2])#returning the median of the middle element
    

#Find quartiles of all elements in the array
def quartile_arr(arr,n):
    arr.sort()#sorting the array
    return ( arr[(n+1)//4], arr[3*(n+1)//4]) #returning the first and third quartile of the array

# quartile deviation of all elements in the array
def fnd_quar_devition(arr, n):
   q1,q3=fnd_quartiles(arr,	n) #calling the function to find the quartiles
   qd=q3-q1#finding the quartile deviation
   return(qd)#returning the quartile deviation





