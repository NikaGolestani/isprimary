num=input("number=")
x=int(num)
arr=[]
firstprimes=[2,3,5,7,11,13,17,19,23]
if x>1:
 for i in firstprimes :
  if x%i==0:
   arr.append(i)
   x=int(x/i)
 while x!=1:
  for i in range(2,x+1):
   if x%i==0:
    if i not in arr:
     arr.append (i)
    x/=i
 for b in arr:
  for a in arr:
   if b%a==0 and a!=b:
    arr.remove(b)
    break
 if len(arr)==1:
  print (f"{num} is a Prime Number")
 elif len(arr)>1:
  print (f"{num} is not a Prime Number.{arr}")
elif x>=0:
 print(f"{num} is not a Prime Number.")
else:
 print("invalid input")
 
