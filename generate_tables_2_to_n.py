# multiplication table from 1 to n
n=int(input("enter how many mul table you want="))
if n<=0:
    print("{} is invalid input".format(n))
else:
    print("-" * 50)
    for i in range(2,n+1):
        print("mul table for={}".format(i))
        print("-" * 50)
        for j in range(1,11):
            print("{} x {} ={}".format(i,j,i*j))
