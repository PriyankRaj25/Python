n=int(input())
array=list(map(int,input().split()))
dict={}
flag=0
for i in array:
  dict[i]=array.count(i)
for key,values in dict:
  if values==1:
    print(key,end=" ")
    flag=1
if flag==0:
  print(-1)
