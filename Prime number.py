n=int(input("Enter how many you want= "))
if n<=0:
    print("{} is invalid input",format(n))
else:
    a=list()
    for i in range(1,n+1):
        val=int(input("Enter {} value= ".format(i)))
        a.append(val)

    else:
        print("values are= ".format(a))

        for num in a:
            if num<=1:
                pass
            else:
                ass="prime number"
                for i in range(2,num):
                    if num%i==0:
                        ass="not prime number"
                        break

                if ass=="prime number":
                    print("{} is prime number".format(num))

                else:
                    print("{} is not prime number".format(num))
