num=input("number=")
x=int(num)
arr=[]
if x>1:
 while x!=1:

  for i in range(2,int(x+1)):
   if x%i==0:
    if i not in arr:
     arr.append (i)
    x/=i
    break
 for b in arr:
  for a in arr:
   if len(arr) > 1 and b%a==0 and a!=b:
    arr.remove(b)
    break
 if len(arr)==1 and arr[0] == int(num):
  print (f"{num} is a Prime Number")
 elif len(arr)>0:
  print (f"{num} is not a Prime Number.{arr}")
elif x>=0:
 print(f"{num} is not a Prime Number.")
else:
 print("invalid input")