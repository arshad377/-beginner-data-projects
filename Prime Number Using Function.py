#first approach
def prime():
    n=int(input("Enter any number = "))
    if n<=1:
        print("{} is invalid input".format(n))
    else:
        ass="prime number"
        for i in range(2,n):
            if n%2==0:
                ass="not prime number"
                break
        if ass=="prime number":
            print("{} is prime number".format(n))
        else:
            print("{} is not prime number".format(n))

#main program
prime()  #function call
