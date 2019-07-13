n=int(input())
array=list(map(int,input().split()))
array.sort(reverse=True)
sum=0
dict={}
for i in array:
  dict[i]=array.count(i)
for key,value in dict.items():
    if key==0:
        for i in range(value):
          sum=sum*10+key
    else:
      sum=sum*10+key
print(sum)
