def triangleNumber(nums):
  nums.sort()

  count = 0
  for i in range(len(nums) - 1, 1, -1):
    left = 0
    right = i - 1
    while left < right:
      if nums[left] + nums[right] > nums[i]:
        count += right - left
        right -= 1
      else:
        left += 1

  return count

nums = [11,4,9,6,15,18]
print(triangleNumber(nums))