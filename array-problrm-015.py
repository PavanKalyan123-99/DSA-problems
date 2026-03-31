nums1=[1,3,5]
nums2=[2,4,6]
i, j = 0, 0
result = []
while i <len(nums1) and j <len(nums2):
    if nums1[i] <nums2[j]:
        result.append(nums1[i])
        i+=1
    else:
        result.append(nums2[j])
        j+=1
while i<len(nums1):
    result.append(nums1[i])
    i+=1
while j<len(nums2):
    result.append(nums2[j])
    j+=1
print(result)