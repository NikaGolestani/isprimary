#manage inputs
num=input("number=")
x=int(num)
arr=[]
#define the range
if x>1:
 while x!=1:
#convert even to odd
  if x%2==0:
   arr.append(2)
   while x%2==0:
    x//=2
#find odd components
  for i in range(3,x+1,2):
   if x%i==0:
    if i not in arr:
     arr.append (i)
    x=x//i
    break
   elif x**0.5<i:
    arr.append(x)
    x=1
    break
#eliminate NOT prime numbers
 for b in arr:
  for a in arr:
   if len(arr) > 1 and b%a==0 and a!=b:
    arr.remove(b)
    break
#print the result
 if len(arr)==1 and arr[0] == int(num):
  print (f"{num} is a Prime Number")
 elif len(arr)>0:
  print (f"{num} is not a Prime Number.{arr}")
#not in range 2->infinity
elif x>=0:
 print(f"{num} is not a Prime Number.")
else:
 print("invalid input")
