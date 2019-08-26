i,r=map(int,input().split())
c=0
for j in range(i,r+1):
  for k in range(1,j): 
    if k*k==j:
        c=c+1
print(c)    
    
    
