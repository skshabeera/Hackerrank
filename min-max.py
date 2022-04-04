n=list(map(int,input("enter the number").split()))
n.sort()
s=sum(n)
max=s-n[0]
min=s-n[len(n)-1]
print(min,max)
