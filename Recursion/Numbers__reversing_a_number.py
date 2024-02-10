def digits(num):
    d=1
    while(num//10!=0):
        d+=1
        num=num//10
    return d
 
def rev_number(num):
    if(num//10==0):
        return num
    else:
        d=digits(rev_number(num//10))
        num1=(num%10)*(10**d)+rev_number(num//10)
        return num1

print(rev_number(12345))
