n=int(input("Enter value of n= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    i=1
    while i<=10:
        print(n,"x",i,"=",n*i)
        i+=1
