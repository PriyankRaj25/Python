n=int(input())
array=list(map(int,input().split()))
flag=0
for i in range(0,n):
  if i==array[i]:
    print(i,end=" ")
    flag=1
if flag==0:
  print(-1)
