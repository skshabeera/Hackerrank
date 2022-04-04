array=list(map(int,input("enter the number").split()))
count=0
i=0
while i<len(array):
    if array[i]==max(array):
        count+=1
    i=i+1
print(count)