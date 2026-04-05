nums = [1,0,-1,0,-2,2]
nums.sort()
result=[]
for i in range(len(nums)-3):
  if i>0 and nums[i]==nums[i-1]:
    continue
  for j in range(i+1, len(nums)-2):
    if j>i+1 and nums[i]==nums[j-1]:
      continue
    left=+1
    right=len(nums)-1
    while left<right:
      sum=nums[i]+nums[j]+nums[left]+nums[right]
      if sum==0:
        result.append([nums[i], nums[j], nums[left], nums[right]])
        while left<right and nums[left]<=nums[left+1]:
          left+=1
        while left<right and nums[left]<=nums[right-1]:
          right-=1
      elif sum<0:
        left+=1
      else:
        right-=1
print(result)

