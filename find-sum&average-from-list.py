n=int(input("enter how many values you want= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    a=[]
    for i in range(1,n+1):
        val=int(input("enter {} value= ".format(i)))
        a.append(val)
    else:
        print("{}".format(a))
        s=0
        n=0
        for val in a:
            if val<0:
              continue
            s=s+val
            n=n+1
        else:
            print("{}".format(s))
            print("{}".format(s/n))
