# find the biggest of three numbers using if else statement
a=int(input("Enter value of a= "))
b=int(input("Enter value of b= "))
c=int(input("Enter value of c= "))

if a>=b and a>c or b<=a>c:
     print("{} is bigger".format(a))
else:
    if b>=c and b>a or a<b>=c:
        print("{} is bigger".format(b))
    else:
        if c>=a and c>b or b<c>=a:
            print("{} is bigger".format(c))
        else:
            if a==b==c:
                print("All are Equal")
