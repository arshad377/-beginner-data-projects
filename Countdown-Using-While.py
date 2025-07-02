n=int(input("Enter value= "))
if n<=0:
    print("{} is invalid input".format(n))
else:
    while n>=1:
        print(n)
        n-=1
