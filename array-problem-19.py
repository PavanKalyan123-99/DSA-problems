s=["h","e","l","l","o"] 
s=list(s)
result=[]
left=0
right=len(s)-1
while left < right:
  s[left], s[right] = s[right], s[left]
  left+=1
  right-=1
print(s)  
