n=int(input("enter value of n= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(0,n,1):
        value=input("enter values= ")
        lst.append(value)
    else:
        print("{} is original list".format(lst))
        lst.sort(reverse=False)
        print("{} is in ascending order".format(lst))
        lst.sort(reverse=True)
        print("{} is in descending order".format(lst))
    print("program completed")
