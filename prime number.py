n=int(input("Enter Any number= "))
if n<=1:
    print("{} is invalid input".format(n))
else:
    ass="prime number"
    for i in range(2,n):
        if n%i==0:
            ass="not prime number"
            break
    if ass=="prime number":
        print("{} is {}".format(n,ass))
    else:
        print("{} is {}".format(n,ass))