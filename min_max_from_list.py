n=int(input("enter values= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("enter {} values=".format(i)))
        lst.append(val)
    else:
        lst.sort()
        print("min is {}".format(lst[0]))
        print("max is {}".format(lst[-1]))
