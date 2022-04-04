a = list(map(int,input("\nEnter the  list  elements: ").split()))
positive_count=0
negative_count=0
zero_count=0
for i in a:
    if i>0:
        positive_count+=1
    elif i<0:
        negative_count+=1
    else:
        zero_count+=1
postive_ratio=positive_count/len(a)
negative_ratio=negative_count/len(a)
zero_ratio=zero_count/len(a)
print(postive_ratio)
print(negative_ratio)
print(zero_ratio)
        

    