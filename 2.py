a,b=map(int,input().split())
n=[int(a) for a in input().split() ]
for i in range(0,len(n)):
    if n[i]==b:
        print("yes")
        break
else:
    print("no")
