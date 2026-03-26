nums = [4,1,2,1,2]
freq={}
for num in nums:
  if num in freq:
    freq[num]+=1
  else:
    freq[num]=1

min_num=None
min_count=0

for num in freq:
   if freq[num]==1:
     print(num)







