a=list(map(int,input("enter the number").split()))
b=list(map(int,input("enter the number").split()))
nas = []
x=0
y=0
for i in range(0,len(a)):
    if a[i]>b[i]:
        x=x+1
    elif b[i]>a[i]:
        y=y+1
    else:
        continue
nas.append(x)
nas.append(y)
print(nas)