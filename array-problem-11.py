nums = [1,-1,3,-2,4]

pos = 0

# move non-negative elements forward
for i in range(len(nums)):
    if nums[i] >= 0:
        nums[pos] = nums[i]
        pos += 1

# now add negatives in order
for i in range(len(nums)):
    if nums[i] < 0:
        nums[pos] = nums[i]
        pos += 1

print(nums)


