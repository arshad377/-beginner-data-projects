n=int(input("Enter value of n= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
