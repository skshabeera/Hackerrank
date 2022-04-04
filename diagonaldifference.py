from operator import length_hint


a=[[1,2,3],[4,5,6],[9,8,9]]
sum=0
sum1=0
i=0
j=-1
while i<len(a):
    sum=sum+a[i][i]
    sum1=sum1+a[i][j]
    j=j-1
    i=i+1
print(abs(sum-sum1))

# 1 2 3
# 4 5 6
# 9 8 9  
