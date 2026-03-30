nums = [3,1,3,2,1]
nums.sort()
pos = 0
for i in range(len(nums)):
  if nums[i]!=nums[pos]:
    pos+=1
    nums[pos]=nums[i]
    
print(pos+1)
print(nums[:pos+1])