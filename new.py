i=int(input())
ar=list(map(int,input().split()))
dict={}
flag=0
for i in ar:
  dict[i]=ar.count(i)
for key,values in dict.items():
  if values>1:
    print(key,end=" ")
    flag=1
if flag==0:
  print("unique")
