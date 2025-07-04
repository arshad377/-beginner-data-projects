#factorial of a number
n=int(input("Enter a number= "))
i=1
fact=1
for i in range(1,n+1):
    fact*=i

print("factorial of {} ={}".format(n,fact))