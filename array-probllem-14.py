nums=[1,0,2,0,3]
pos=0
for i in range(len(nums)):
  if nums[i]==0:
    nums[pos]=nums[i]
    pos+=1
for i in range(pos, len(nums)):
  nums[i]!=0
print(nums) 


