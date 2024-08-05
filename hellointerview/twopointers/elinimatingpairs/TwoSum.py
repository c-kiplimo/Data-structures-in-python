def isPairSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

nums = [1, 3, 4, 6, 8, 10, 13]
target = 13
print(isPairSum(nums, target))  


##

def twoSum(nums,target):
    left,right =0,len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True
        if current_sum < target:
            left +=1
        else:
            right -=1
    return False

nums = [1, 3, 4, 6, 8, 10, 13]
target = 13
print(twoSum(nums, target)) 
    
