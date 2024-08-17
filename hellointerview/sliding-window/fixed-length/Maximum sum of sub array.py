def max_subarray_sum(nums, k):
  max_sum = 0
  state = 0
  start = 0

  for end in range(len(nums)):
    state += nums[end]

    if end - start + 1 == k:
      max_sum = max(max_sum, state)
      state -= nums[start]
      start += 1

  return max_sum