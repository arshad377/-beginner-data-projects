 find the max and min value from a list
n=int(input("enter value of n= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    we=[]
    for i in range(1,n+1):
        val=int(input("enter {} value= ".format(i)))
        we.append(val)
    else:
        maxv=we[0]
        minv=we[0]
        for val in we:
            if val>maxv:
                maxv=val
            if val<minv:
                minv=val
        else:
            print("max={}".format(maxv))
            print("maxv=%d" %minv)
