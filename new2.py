n=int(input())
array=list(map(int,input().split()))
array.sort(reverse=True)
sum=0
dict={}
for i in array:
  dict[i]=i
for key,value in dict.items():
  sum=sum*10+key
print(sum)
