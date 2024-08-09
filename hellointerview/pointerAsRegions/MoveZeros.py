def moveZeroes(nums):
    nextNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1

nums = [2, 0, 4, 0, 9]

moveZeroes(nums)
print(nums)
