while True:
    num=int(input('num='))
    if num>1:
        arr=[]
        for i in range(2,round((num/2)+1)):
            if num%i==0:
                arr.append(i)
            lenarr=len(arr)
            while lenarr>0:
                for x in arr:
                    for y in arr:
                        if y==x:
                            continue
                        elif y % x == 0:
                            arr.remove(y)

                lenarr-=1

        if len(arr)!=0:
            print(f'{num} is not a prime number \n {num}:{arr}')
        else:
            print(f'{num} is a prime number')
    elif num<0:
        print(f'{num} is an invalid input')
    else:
        print(f'{num} is not a prime number')
