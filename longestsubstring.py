

str="greeksforgreeks"
i=0
count=0
l=[]
for i in str:
    if i not in l:
        l.append(i)
        b=len(l)
print(b)
