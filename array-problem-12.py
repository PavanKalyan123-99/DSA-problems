nums = [1,2,3,4,5,6]
temp = nums[:]   # copy original

pos = 0

for i in range(len(nums)):
    if temp[i] % 2 == 0:
        nums[pos] = temp[i]
        pos += 1

for i in range(len(nums)):
    if temp[i] % 2 != 0:
        nums[pos] = temp[i]
        pos += 1

print(nums)