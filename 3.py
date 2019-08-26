n=int(input())
b=[]
a=[int(n) for n in input().split()]
if len(a)%2==0:
    for i in range(0,len(a)-1,2):
        b.append(a[i+1])
        b.append(a[i])
else:
    for i in range(0,len(a)-1,2):
        b.append(a[i+1])
        b.append(a[i])
    b.append(a[-1])
for j in range(0,len(b)):
    print(b[j],end=" ")
    
    
