def digits(num):#function to find the number of digits in a number
    d=1#initializing the number of digits to 1
    while(num//10!=0):#loop to find the number of digits
        d+=1#incrementing the number of digits
        num=num//10#reducing the number
    return d#returning the number of digits
 
def rev_number(num):#function to reverse a number
    if(num//10==0):#base case
        return num#returning the number if it has only one digit
    else:
        d=digits(rev_number(num//10))#finding the number of digits in the number
        num1=(num%10)*(10**d)+rev_number(num//10)#returning the reverse of the number
        return num1

print(rev_number(12345))
